from langchain_community.document_loaders import TextLoader
data = TextLoader("document_loaders/notes.txt")

docs=data.load()
print(docs)          # full document object
print(len(docs))     # number of documents
print(docs[0].page_content)   # the actual text
print(docs[0].metadata)       # file path metadata
print("1st:",docs[0])