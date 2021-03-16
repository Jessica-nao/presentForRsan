import requests
from bs4 import BeautifulSoup

res = requests.get('https://kenkoooo.com/atcoder/#/contest/show/215dbebf-6fda-4a1d-a90f-7f539755f039')

print(res.text)

# soup = BeautifulSoup(res.text, 'html.parser')

# links = [url.get('href') for url in soup.find_all('a')]
# print(links)