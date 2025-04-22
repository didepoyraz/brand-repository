import requests
from bs4 import BeautifulSoup

def get_og_title(url):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        og_title = soup.find("meta", property="og:title")
        return og_title["content"] if og_title else soup.title.string
    except:
        return None
