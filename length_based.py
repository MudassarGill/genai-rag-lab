from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate,PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableLambda,RunnableBranch
from langchain_text_splitters import CharacterTextSplitter

load_dotenv()

#demo txt
text="""
    I am a software engineer with 5 years of experience in the software industry.
     I have worked on various projects and technologies, including web development,
      mobile development, and cloud computing. I am a quick learner and can pick up 
      new technologies quickly. I am also a team player and enjoy working in a collaborative environment. 
      I am looking for a challenging role where I can utilize my skills and experience to contribute to the success of the organization.
"""

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=''
)

chunks=splitter.split_text(text)

print(chunks)