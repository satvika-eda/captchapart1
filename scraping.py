import requests
from bs4 import BeautifulSoup

def filename(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find('img')
    return result['src']