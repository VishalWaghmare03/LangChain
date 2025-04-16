# before "pip install pypdf"
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/home/vishal/Downloads/CampusX DLCV Course Syllabus.pdf')

docs = loader.load()

print(docs[0].page_content)

print("====================================================================================================================")

print(docs[0].metadata)