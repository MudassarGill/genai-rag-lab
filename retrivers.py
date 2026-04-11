from langchain_community.retrievers import WikipediaRetriever
from langchain_openai import OpenAIEmbeddings

retrivers=WikipediaRetriever(top_k_results=2)
query='What is AI and tell me its types?'
docs=retrivers.invoke(query)


for i , doc e(docs):
    print()