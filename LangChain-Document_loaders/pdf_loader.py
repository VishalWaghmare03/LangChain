# before "pip install pypdf"
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/home/vishal/Downloads/17.-Shareholders-Agreement_3726.pdf')

docs = loader.load()

print(docs[1].page_content)

print("====================================================================================================================")

print(docs[1].metadata)