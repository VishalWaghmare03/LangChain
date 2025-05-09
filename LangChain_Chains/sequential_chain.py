from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a detailed report on  {topic}",
    input_variables=["topic"] 
)

prompt2 = PromptTemplate(
    template="Generate a 5 pointer summary from the following text \n {topic}",
    input_variables=["text"] 
)

model = ChatOpenAI(model='gpt-4.1-nano')

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'India in AI'})

print(result)

chain.get_graph().print_ascii()