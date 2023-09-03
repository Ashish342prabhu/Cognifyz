import requests
from bs4 import BeautifulSoup

def scrape_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('span', class_='text')
        authors = soup.find_all('small', class_='author')
        for i in range(len(quotes)):
            print(f"Quote: {quotes[i].text}")
            print(f"Author: {authors[i].text}\n")
    else:
        print("Failed to retrieve the web page.")

if __name__ == "__main__":
    url = "http://quotes.toscrape.com"
    scrape_quotes(url)
