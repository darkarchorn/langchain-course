from langchain import hub
from langchain_classic.agents import AgentExecutor
from langchain_classic.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS
from schema import AgentResponse

tools = [TavilySearch()]
llm = ChatOpenAI(base_url="localhost:1234/v1", model="model-name", verbose=True)
react_prompt = hub.pull("hwchase17/react")
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)
react_prompt_with_format_instructions = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input", "agent_scratchpad", "tool_names"],
).partial(format_instructions=output_parser.get_format_instructions())


agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt,
    prompt=react_prompt_with_format_instructions,
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, callbacks=True, max_iterations=3)
chain = agent_executor
extract_output = RunnableLambda(lambda x: x["output"])
parse_output = RunnableLambda(lambda x: output_parser.parse(x))
chain = agent_executor | extract_output | parse_output


def main():
    result = chain.invoke()
    print(result)
