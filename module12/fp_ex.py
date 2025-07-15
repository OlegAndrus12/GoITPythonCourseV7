import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def fetch(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")

def print_quote():
    pass

def get_all_quotes(soup: BeautifulSoup) -> List[Dict]:
    quotes_data = []
    quote_divs = soup.find_all("div", class_="quote")
    for quote_div in quote_divs:
        text = quote_div.find("span", class_="text")
        author = quote_div.find("small", class_="author")
        tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]
        quotes_data.append({
            "text": text.text if text else "No quote text found",
            "author": author.text if author else "Unknown author",
            "tags": tags
        })
    return quotes_data

# Usage
url = "https://quotes.toscrape.com/"
html = fetch(url)
soup = parse(html)
all_quotes = get_all_quotes(soup)

for i, q in enumerate(all_quotes, 1):
    print(f"\nQuote {i}:")
    print("Text:", q["text"])
    print("Author:", q["author"])
    print("Tags:", q["tags"])
