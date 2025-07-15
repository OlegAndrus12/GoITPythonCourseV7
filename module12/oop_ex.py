import requests
from bs4 import BeautifulSoup

class Quote:
    def __init__(self, id, text, author, tags):
        self.id = id
        self.text = text
        self.author = author
        self.tags = tags
    
    def __repr__(self):
        return f"Quote #{self.id}: by {self.author}"
    
    def __str__(self):
        return self.text


class QuoteScraper:
    def __init__(self, url):
        self.url = url
        self.html = None
        self.soup = None

    def fetch(self):
        response = requests.get(self.url)
        response.raise_for_status()
        self.html = response.text

    def parse(self):
        if self.html is None:
            raise ValueError("No HTML to parse, call fetch() first")
        self.soup = BeautifulSoup(self.html, "html.parser")

    def get_all_quotes(self):
        if self.soup is None:
            raise ValueError("No soup parsed, call parse() first")
        quotes_data = []
        quote_divs = self.soup.find_all("div", class_="quote")

        for i, quote_div in enumerate(quote_divs):
            text = quote_div.find("span", class_="text")
            author = quote_div.find("small", class_="author")
            tags = [tag.text for tag in quote_div.find_all("a", class_="tag")]
            data = {
                "id": i,
                "text": text.text if text else "No quote text found",
                "author": author.text if author else "Unknown author",
                "tags": tags
            }
            quotes_data.append(Quote(**data))
        return quotes_data

# Usage
scraper = QuoteScraper("https://quotes.toscrape.com/")
scraper.fetch()
scraper.parse()
all_quotes = scraper.get_all_quotes()
print(all_quotes[0].author)