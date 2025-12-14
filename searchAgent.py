from dotenv import load_dotenv

load_dotenv()
from typing import Dict, List, Optional

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field
from tavily import TavilyClient

from cvtext import cvtext

tavily = TavilyClient()

class PastWorkResponse(BaseModel):
    name:str = Field(default_factory=str, description="The name of the applicant")
    projects:List[Field] = Field(default_factory=list, description="The projects that the applicant had worked on at the company")
    position:str = Field(default_factory=str, description="The position of the applicant at the company, e.g Software Engineer, Data Analyst,...")
    startDate:int = Field(default_factory=int, description="The start year of the applicant in that company")
    endDate:int = Field(default_factory=int, description="The last year of the applicant in that company")
    reason:str = Field(default_factory=str, description="The potential reason that the applicant left the company (or the reason they want to find a new job)")

class AgentResponse(BaseModel):
    name:str = Field(default_factory=str, description="The name of the applicant")
    birth:str = Field(default_factory=str, description="The birthday of the applicant in yyyyMMdd format, if empty then leave it as an empty string")
    gender:int = Field(default_factory=int, description="The gender of the applicant, 0 for male, 1 for female and 2 for other genders if they specifically specify it")
    residence:str = Field(default_factory=int, description="The residence of the applicant")
    skills:List[Field] = Field(default_factory=list, description="The list of programming languages that the applicant has")
    places:List[PastWorkResponse] = Field(default_factory=PastWorkResponse, description="The places that the applicant had worked at and the places' information")
    yoe:float = Field(default_factory=float, description="The number of year that the applicant had their experience in the industry")
    education:str = Field(default_factory=str, description="The university/campus that the application had gone through/ currently enrolling")
    position:str = Field(default_factory=str, description="The position that the applicant is seeking")
    certs:List[str] = Field(default_factory=list, description="List of certifications that the applicant has")
    awards:List[str] = Field(default_factory=list, description="List of awards that the applicant has")

llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="gpt-oss-20b"
)
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools, response_format=AgentResponse)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="What are the skills that this person have")})
    print(result['structured_response'])

main()

#ten, birth, sex, resident, past work places{name of the place, name of project, position, time at the place, reason of leaving}, yoe(total) int, edu, awards[], cert[], apply position[]