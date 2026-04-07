from langchain_community.document_loaders import TextLoader

loader = TextLoader("sample_data.txt")
documents = loader.load()
print(documents[0])
print(len(documents))