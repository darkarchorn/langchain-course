import asyncio
import json
import numpy as np

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
import redis.asyncio as redis

from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_classic.embeddings import HuggingFaceEmbeddings

# =========================
# CONFIG
# =========================

REDIS_URL = "redis://localhost:6379"
MAX_CONCURRENT_REQUESTS = 2

LM_STUDIO_BASE_URL = "http://localhost:1234/v1"
MODEL_NAME = "abc"

DOCUMENT = """
Redis is an in-memory data structure store used as a database,
cache, and message broker.
"""

# =========================
# APP + REDIS
# =========================

app = FastAPI()
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

SEMAPHORE_KEY = "llm:semaphore"
CACHE_PREFIX = "semantic:"

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# =========================
# REDIS SEMAPHORE
# =========================

async def acquire_slot():
    while True:
        count = await redis_client.incr(SEMAPHORE_KEY)
        if count <= MAX_CONCURRENT_REQUESTS:
            return
        await redis_client.decr(SEMAPHORE_KEY)
        await asyncio.sleep(0.2)

async def release_slot():
    await redis_client.decr(SEMAPHORE_KEY)

# =========================
# SEMANTIC CACHE (LOCAL)
# =========================

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

async def semantic_cache_search(question: str, threshold=0.8):
    q_vec = embeddings.embed_query(question)
    keys = await redis_client.keys(f"{CACHE_PREFIX}*")

    for key in keys:
        data = json.loads(await redis_client.get(key))
        if cosine(q_vec, data["vector"]) >= threshold:
            return data["answer"]

    return None

async def semantic_cache_set(question: str, answer: str):
    vec = embeddings.embed_query(question)
    key = f"{CACHE_PREFIX}{hash(question)}"
    await redis_client.set(key, json.dumps({
        "vector": vec,
        "answer": answer
    }))

# =========================
# ENDPOINT
# =========================

@app.post("/ask")
async def ask(request: Request):
    body = await request.json()
    question = body["question"]

    # 1️⃣ CACHE CHECK
    cached = await semantic_cache_search(question)
    if cached:
        async def cached_stream():
            yield cached
        return StreamingResponse(cached_stream(), media_type="text/plain")

    # 2️⃣ QUEUE
    await acquire_slot()

    callback = AsyncIteratorCallbackHandler()

    llm = ChatOpenAI(
        model=MODEL_NAME,
        base_url=LM_STUDIO_BASE_URL,
        api_key="not-needed",
        streaming=True,
        callbacks=[callback],
        temperature=0,
    )

    prompt = f"""
Answer ONLY using the document.

DOCUMENT:
{DOCUMENT}

QUESTION:
{question}
"""

    async def stream():
        full_answer = ""
        try:
            task = asyncio.create_task(
                llm.agenerate([[HumanMessage(content=prompt)]])
            )

            async for token in callback.aiter():
                full_answer += token
                yield token

            await task

            # 3️⃣ SAVE TO CACHE
            await semantic_cache_set(question, full_answer)

        finally:
            await release_slot()

    return StreamingResponse(stream(), media_type="text/plain")

# =========================
# HEALTH CHECK
# =========================

@app.get("/health")
def health():
    return {"status": "ok"}
