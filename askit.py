import django
from autocorrect import Speller
from ScrapeSearchEngine.SearchEngine import Google
from webpage_reader import analyse, read_page

# The command below from the autocorrect module creates a function which can then be used to correct spelling from user-inputed strings
spell = Speller()

chat = "default startup text"

chat = input("Enter:")
gg = spell(chat)
# The command below searches google 
gg_searched = Google(gg, "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.0.02")

# The block of code below analyzes the webpages
url=gg_searched[1]
headers = {}
page_text = read_page(url=url, headers=headers)
result = analyse(page_text=page_text, url=url)
print(result)