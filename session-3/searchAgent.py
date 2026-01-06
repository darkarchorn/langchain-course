from dotenv import load_dotenv

load_dotenv()
from pydantic import BaseModel, Field
from typing import List
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from langchain_tavily import TavilySearch

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """
    print(f"Searching for {query}")
    return tavily.search(query)

class City(BaseModel):
    """The city information"""
    name:str = Field(default="", description="The city's name")
    country:str = Field(default="", description="The city's country")

class AirQualityResponse(BaseModel):
    """The schema for user's query's response"""
    city:City = Field(default=None, description="The city that the agent is referring to")
    date:str = Field(default="1970/01/01", description="The date of the calculation")
    humidity:float = Field(default=0.0, description="The humidity of the city")
    temp:float = Field(default=0.0, description="The temperature of the city in degree C")

class ListAirQuality(BaseModel):
    """The response schema for user's query"""
    response:List[AirQualityResponse] = Field(default_factory=list, description="The response in list for user's query")

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="gpt-oss-20b"
)
# tools = [search]
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=ListAirQuality)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Give me the air quality of 3 random city in")})
    print(result)

main()