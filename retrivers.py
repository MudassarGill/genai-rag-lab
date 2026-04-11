from langchain_community.retrievers import WikipediaRetriever
from langchain_openai import OpenAIEmbeddings

retrivers=WikipediaRetriever(top_k_results=2)
query='What is AI and tell me its types?'
docs=retrivers.invoke(query)

for i , doc in  enumerate(docs):
    print(f'\n----Resutl {i+1}----')
    print(f'content --> \n {doc.page_content}..')