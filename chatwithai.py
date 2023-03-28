import openai
from flask import Flask, render_template, blueprints
from flask_sqlalchemy import SQLAlchemy 

return render_template("chatwithai.html")

app.config ["SQLALCHEMY_DATABSE_URL"] = "sqlite:///chatwithai.db"
db = SQLAlchemy(app)

class User(db.Model):
    global user
    user = db.Column(db.String(200), nullable=False)

openai.api_key = "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"
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: {27/3/23} Current date: {26/3/23}"},
        {"role": "user", "content": user},
        {"role": "assistant", "content": "Hi user, your question delights me the answer is:"},
    ]
)

reply_content = response['choices'][0]['message']['content']
print(reply_content)