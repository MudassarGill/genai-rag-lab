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
doc4=Document(
    page_content="Mohammad Amir is a very good bowler.He is very fast bowler He is very populer in the world.",
    metadata={
        "source": "doc4",
        "author": "M Mudassar Hussain"
    }
)
doc5=Document(
    page_content="shaheen shah afridi is a very good bowler.He is very fast bowler He is very populer in the world.",
    metadata={
        "source": "doc5",
        "author": "M Mudassar Hussain"
    }
)

docs=[doc1,doc2,doc3,doc4,doc5]

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": False},
)

vectorstore=Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./.My_chroma_db",
    collection_name="cricket"
)
vectorstore.add_documents(docs)
#view doc embding,metadata
print(vectorstore.get(include=["documents","metadatas","embeddings"]))
print("Vector store created successfully")


vectorstore.similarity_search(
    "who among these are a bowler?",
    k=2
)

vectorstore.similarity_search_with_score(
    "who among these are a batsman?",
    k=2
)

vectorstore.similarity_search_with_score(
    "who is the best batsman?",
    k=2
)
vectorstore.get(include=["documents","metadatas","embeddings"])