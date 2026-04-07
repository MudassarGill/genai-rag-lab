from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableLambda,RunnableBranch

load_dotenv()

loader = WebBaseLoader("https://en.wikipedia.org/wiki/Artificial_intelligence")
documents = loader.load()


model=ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0
)

prompt=PromptTemplate(
    input_variables=["context","question"],
    template="""
    Use the following context to answer the question.
    Context: {context}
    Question: {question}
    """
)

parser=StrOutputParser()

chain=prompt | model | parser

print(chain.invoke({"context":documents[0].page_content,"question":"What is Artificial Intelligence?"}))