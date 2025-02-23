from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is capital of India",
    "Mumbai is the Financial Capital of India",
    "Pune is the fastest growing city in the India"
]

# this function having the capability of generate the embedding of multiple document at a time.
result = embedding.embed_documents(documents)

print(str(result))