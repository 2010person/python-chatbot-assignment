from flask import Flask, request, render_template
import openai

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatwithai", methods=["POST", "GET"])
def chatwithai():

    if request.method == "POST":
        openai.api_key = "OPENAIAPIKEY"

        prompt = request.form.get("text_input")

        params = {
            "temperature": 0.5,
            "max_tokens": 100,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        response = openai.Completion.create(engine="davinci", prompt=prompt, **params)

        user_question = prompt
        ai_response = response.choices[0].text.strip()


        return render_template("chatwithai.html", user=user_question, ai=ai_response)

    else:
        return render_template('chatwithai.html')