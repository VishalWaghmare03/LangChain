from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

prompt = PromptTemplate(
    template="Write a summary for the following details -\n {data}",
    input_variables=['data']
)

parser = StrOutputParser()


loader = TextLoader('/home/vishal/Downloads/Data_Analysis_Forklift_Model.txt', encoding='utf-8')

docs = loader.load()

# print(type(docs))   # ---> <class 'list'>

# print(len(docs))     # ---> 1

# print(type(docs[0]))     # ---> <class 'langchain_core.documents.base.Document'>


print(docs[0].page_content)


print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'data':docs[0].page_content}))