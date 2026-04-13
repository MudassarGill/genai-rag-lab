
from langchain.tools import BaseTool
from typing import type
from pydantic import Field,BaseModel



class Multipleinput(BaseModel):
    a: int = Field(required=True,description="First number")
    b: int = Field(required=True,description="Second number")


class Multiplytools(BaseTool):
    name: str = "Multiply"
    description: str = "Multiply two numbers"
    args_schema: type[BaseTool] = Multipleinput
    def _run(self,a:int,b:int)->int:
        return a*b
    def _arun(self,a:int,b:int)->int:
        return a*b


mul=Multiplytools()
result=mul.invoke({"a":2,"b":3})
print(result)
print(mul.name)
print(mul.description)
print(mul.args_schema)
    