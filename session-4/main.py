from dotenv import load_dotenv

load_dotenv()

from langchain_classic import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from schemas import Source, AgentReponse
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS

tools = [TavilySearch()]
react_prompt = hub.pull("hwchase17/react")
output_parser = PydanticOutputParser(pydantic_object=AgentReponse)
react_prompt_with_format_instructions = PromptTemplate(template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS)

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="gpt-oss-20b"
)

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

chain = agent_executor 

def main():
    print("Main is running ...")
    result = chain.invoke(
        input={
            "input": "what is 1+1",
        }
    )
    print(result)

if __name__ == "__main__":
    main()