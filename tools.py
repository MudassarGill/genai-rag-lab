from langchain.tools import tool

@tool
def add(a:int,b:int)->int:
    """Add two numbers"""
    return a+b

@tool
def sub(a:int,b:int)->int:
    """Subtract two numbers"""
    return a-b

@tool
def mul(a:int,b:int)->int:
    """Multiply two numbers"""
    return a*b

@tool
def div(a:int,b:int)->int:
    """Divide two numbers"""
    return a/b
