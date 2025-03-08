from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')

# schema
class Review(TypedDict):
    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great, but software feels bloated.
                                 There are too many pre-installed apps that I can't remove. Also, the UI looks outdated
                                 compared to other brands. Hoping for a software update to fix this.""")

print(f'Result ::: {result}')
# print(f'Output Data Type ::: {type(result)}')
# print(f'Only Summary ::: {result['summary']}')
# print(f'Only Sentiment ::: {result['sentiment']}')
# print(result['summary'])
# print(result['sentiment'])





# Behind the seen what::: here haven't return anything in the prompt but it works like below
# You are an AI assistant that extracts structured insights from text. Given a product review, 
# extract: - Summary: A brief overview of the main points.
# Sentiment: Overall tone of the review(positive, neutral, negative). Return the response in JSON format.
# :::::::::::::::::: then Prompt :::::::::::::::::::::::::::::::::::::::