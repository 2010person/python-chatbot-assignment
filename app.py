from flask import Flask, request, render_template
from ScrapeSearchEngine.ScrapeSearchEngine import Google
from bs4 import BeautifulSoup
import openai
import os
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chatwithai", methods=["POST", "GET"])
def chatwithai():

    if request.method == "POST":
        openai.api_key = os.getenv("OPENAIAPIKEY")

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
    
@app.route("/askit", methods=["POST", "GET"])
def askit():
    if request.method == "POST":
        chat = request.form.get("text_input")
        # The command below searches google
        gg_searched = Google(chat, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0  x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.0.0")
        # Below we analyze the webpages that has been found on Google
        thing = gg_searched[0]
        PAGE = requests.get(thing)
        SOUP = BeautifulSoup(PAGE.text, 'html.parser')
        text = SOUP.get_text()

        return render_template("askit.html", user=chat, scrape=text)
    
    else:
        return render_template("askit.html")
    
def create_app(app_name="python-chatbot-assignment"):
  app = Flask(app_name)
  app.config.from_object('api.config.DevelopmentConfig')

  from api.api import api
  app.register_blueprint(api, url_prefix='/api')

  from api.models import db
  db.init_app(app)

  return app
