from langchain.tools import BaseTool
from typing import type



class MultipleTool(BaseTool):
    a: int = Field(description="First number")
    b: int = Field(description="Second number")
    name: str = "Multiple"
    description: str = "Multiply two numbers"
    def _run(self,a:int,b:int)->int:
        return a*b
    def _arun(self,a:int,b:int)->int:
        return a*b
