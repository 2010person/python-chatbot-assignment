import openai
from flask import Flask 

user = str(input("Enter:"))

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: {24/3/23} Current date: {25/3/23}"},
        {"role": "user", "content": user},
        {"role": "assistant", "content": "Hi user, your question delights me the answer is:"},
    ]
)