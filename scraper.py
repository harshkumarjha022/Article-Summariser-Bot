import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
        return "\n".join(paragraphs)
    except Exception as e:
        print(f"Error scraping URL {url}: {e}")
        return None
