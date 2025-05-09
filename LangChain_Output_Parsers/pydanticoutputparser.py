from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

load_dotenv()

# # Define the model
# llm = HuggingFaceEndpoint(
#     repo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     text="text-generation"
# )

# model_1 = ChatHuggingFace(llm=llm)

model = ChatOpenAI(model="gpt-4o-mini")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age, and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# place = str(input("Enter the place : "))

# prompt = template.invoke({'place':place})

# print(prompt)

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)


## With Chain

chain = template | model |parser

final_result = chain.invoke({'place','sri lankan'})

print(final_result)