from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini', temperature=1.5)

result = model.invoke("write a 5 line poem on cricket")

print(result.content)