import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")    

question = input("What would you like to ask: ")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a ChatBot"},
        {"role": "user", "content": f"{question}"},
    ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(f"We asked chatGPT {question} - here is their response: ")
print(result)   


