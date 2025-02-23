from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is capital of India",
    "Mumbai is the Financial Capital of India",
    "Pune is the fastest growing city in the India"
]

vector = embedding.embed_documents(documents)

print(str(vector))