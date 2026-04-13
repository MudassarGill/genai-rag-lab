from langchain.tools import tool

@tool
def Mutliple(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

@tool
def divide(a:int,b:int)->int:
    """Divide two numbers"""
    return a/b

@tool
def add(a:int,b:int)->int:
    """Add two numbers"""
    return a+b

@tool
def sub(a:int,b:int)->int:
    """Subtract two numbers"""
    return a-b


class toolkit:
    def combine_tools(self):
        return [Mutliple,divide,add,sub]

toolkit=toolkit()
print(toolkit.combine_tools())