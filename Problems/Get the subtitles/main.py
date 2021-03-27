import requests

from bs4 import BeautifulSoup

numh = int(input())
url1 = str(input())
r = requests.get(url=url1)
s = BeautifulSoup(r.content, 'html.parser')
subtitle = s.findAll('h2')
print(subtitle[numh].text)
