from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
from langchain_core.documents import Document
load_dotenv()

doc1=Document(
    page_content="Babar azam is a very good batsman.He is very good at cover drive. and Fakhar Zaman is a very good batsman.",
    metadata={
        "source": "doc1",
        "author": "M Mudassar Hussain"
    }
)

doc2=Document(
    page_content="Shoaib Akhtar is a very good bowler.He is very fast bowler He is very populer in the world.",
    metadata={
        "source": "doc2",
        "author": "M Mudassar Hussain"
    }
)

doc3=Document(
    page_content="Wasim Akram is a very good bowler.He is very fast bowler He is very populer in the world.",
    metadata={
        "source": "doc3",
        "author": "M Mudassar Hussain"
    }
)

docs=[doc1,doc2,doc3]

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": False},
)

vectorstore=Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./.chroma_db"
)