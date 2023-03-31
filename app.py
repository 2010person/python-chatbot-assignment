from flask import Flask, request, render_template
import openai

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatwithai", methods=["POST", "GET"])
def chatwithai():

    openai.api_key = "OPENAIAPIKEY"

    prompt = request.form['prompt']
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = {'user': prompt, 'ai': response.choices[0].text}

    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=False)