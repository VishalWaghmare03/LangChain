from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
from langchain_openai import ChatOpenAI


load_dotenv()

# print("TOKEN:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))


# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation"
# )

# model = ChatHuggingFace(llm=llm)
model = ChatOpenAI(model="gpt-4.1-nano")

parser = JsonOutputParser()

template = PromptTemplate(
    template = "Give me 5 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)


# Below code with chains.
chain = template | model | parser

# If we are not giving any input then we have to give blank dictionary as input.
result = chain.invoke({'topic':'black hole'})

print(result)
print(type(result))





# prompt = template.format()
# # print(prompt)

# result = model.invoke(prompt)
# # print(result.content)

# final_result = parser.parse(result.content)

# print(final_result)
# print(type(final_result))



# ** Here we can't assign any schema or structure to output be in. SO WE HAVE TO USE DIFFERENT TECHINIQUE FOR THE SPECIFIC SCHEMA
# ** using the parser we are saying to give the output as json object.