from ScrapeSearchEngine.ScrapeSearchEngine import Google
import requests
from bs4 import BeautifulSoup

chat = "default startup text"

def process_questions():
    global chat
    chat = input("Enter:")
    # The command below searches google
    gg_searched = Google(chat, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0  x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.0.0")
    # Below we analyze the webpages that has been found on Google
    PAGE = requests.get(gg_searched[0])
    SOUP = BeautifulSoup(PAGE.text, 'html.parser')
    for TAG in SOUP.find_all('p'):
        if TAG.string is not None:
            print(TAG.string)
        
process_questions()