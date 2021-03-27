import requests

from bs4 import BeautifulSoup
import re

word = str(input())
url1 = str(input())
r = requests.get(url=url1)
s = BeautifulSoup(r.content, 'html.parser')
print(s.find('p', text=re.compile(f'.*{word}.*')).text)
