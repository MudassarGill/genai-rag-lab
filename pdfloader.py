from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableLambda,RunnableBranch
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader("M Mudassar Hussain.pdf")
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

print(chain.invoke({"context":documents[0].page_content,"question":"Tell me Mudassar Hussain education and univeristy name"}))