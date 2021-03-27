import requests

from bs4 import BeautifulSoup


act_num = int(input())
url1 = str(input())

r = requests.get(url=url1)
s = BeautifulSoup(r.content, 'html.parser')
acts = s.findAll('a')
res = acts[act_num - 1]
print(res['href'])
