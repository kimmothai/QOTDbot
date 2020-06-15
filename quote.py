import requests
import random

### Variables ###
quote_url = "https://taskinoz.com/gdq/api/"
motivation_url = "https://type.fit/api/quotes"


def get_quote():
    # Retrieves a random generated Games Done Quick donation message style text
    response = requests.get(quote_url)
    quote = response.text
    return quote


def fix_author(author):
    # Replace empty author with "Unknown" to improve output.
    if author == None:
        author = "Unknown"
    return author


def get_motivated():
    # Retrieves a random insightful quote from the website
    response = requests.get(motivation_url)
    content = random.choice(response.json())
    content["author"] = fix_author(content["author"])
    return content
