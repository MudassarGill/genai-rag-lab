from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableLambda,RunnableBranch
from langchain_text_splitters import CharacterTextSplitter,RecursiveCharacterTextSplitter,Language

load_dotenv()   

text="""
  class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    def set_name(self,name):
        self.name=name

    def set_age(self,age):
        self.age=age
    
"""

splitter=RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", ".", " "],
    chunk_size=100,
    chunk_overlap=20,
)

chunks=splitter.split_text(text)

print(chunks)