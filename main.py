from dotenv import load_dotenv

load_dotenv()
from typing import Dict, List, Optional

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from pydantic import BaseModel, Field
from tavily import TavilyClient

from cvtext import cvtext

tavily = TavilyClient()

class PastWorkResponse(BaseModel):
    name:str = Field(default="", description="The name of the applicant")
    projects:List[str] = Field(default_factory=list, description="The projects that the applicant had worked on at the company")
    position:str = Field(default="", description="The position of the applicant at the company, e.g Software Engineer, Data Analyst,...")
    startDate: Optional[int] = Field(default=None, description="Start year")
    endDate: Optional[int] = Field(default=None, description="End year")
    reason:str = Field(default="", description="The potential reason that the applicant left the company (or the reason they want to find a new job)")

# class AgentResponse(BaseModel):
#     name:str = Field(default="", description="The name of the applicant")
#     birth:str = Field(default="", description="The birthday of the applicant in yyyyMMdd format, if empty then leave it as an empty string")
#     gender:int = Field(default=-1, description="The gender of the applicant,-1 for unknown, 0 for male, 1 for female and 2 for other genders if they specifically specify it")
#     residence:str = Field(default="", description="The place of residence of the applicant")
#     skills:List[str] = Field(default_factory=list, description="The list of programming languages that the applicant has")
#     places:List[PastWorkResponse] = Field(default_factory=list, description="The places that the applicant had worked at and the places' information")
#     yoe:float = Field(default=0.0, description="The number of year that the applicant had their experience in the industry")
#     education:str = Field(default="", description="The university/campus that the application had gone through/ currently enrolling")
#     position:str = Field(default="", description="The position that the applicant is seeking")
#     certs:List[str] = Field(default_factory=list, description="List of certifications that the applicant has")
#     awards:List[str] = Field(default_factory=list, description="List of awards that the applicant has")

class AgentResponse(BaseModel):
    name: str = ""
    birth: str = ""
    gender: int = -1
    residence: str = ""
    skills: List[str] = []
    places: List[PastWorkResponse] = []
    yoe: float = 0.0
    education: str = ""
    position: str = ""
    certs: List[str] = []
    awards: List[str] = []



def main():
    prompt = f"""
    Extract structured information from the following CV.

    Rules:
    - If information is missing, use empty string, empty list, or null.
    - Do NOT guess dates or gender.
    - Skills must be programming languages, frameworks, or tools only.

    CV:
    {cvtext}
    """
    llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio",
    model="gpt-oss-20b",
    temperature=0
    )

    structured_llm = llm.with_structured_output(AgentResponse)
    print(structured_llm.invoke(prompt))



if __name__ == "__main__":
    main()