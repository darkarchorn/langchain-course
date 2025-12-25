from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

tools = [TavilySearch()]

llm = ChatOpenAI(
    base_url="http://10.64.130.106:11434",
    model="qwen2.5:3b",
    temperature=0,
)

react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=3,
)

def main():
    result = agent_executor.invoke({
        "input": "What is LangChain and who created it?"
    })
    print(result["output"])

if __name__ == "__main__":
    main()
