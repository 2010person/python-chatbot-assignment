from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import openai

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatwithai", methods=["POST", "GET"])
def chatwithai():
    global content

    if request.method == 'POST':
        content = request.form["content"]

    openai.api_key = "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"

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible. Knowledge cutoff: {27/3/23} Current date: {26/3/23}"},
            {"role": "user", "content": content},
            {"role": "assistant", "content": "Hi user, your question delights me the answer is:"},
        ]
    )

    reply_content = response['choices'][0]['message']['content']

    return render_template("chatwithai.html")

if __name__ == "__main__":
    app.run(debug=False)