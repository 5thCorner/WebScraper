import requests
from bs4 import BeautifulSoup
import string
import os


def format_title(title):
    for ch in title:
        if ch in string.punctuation + '’':
            title = title.replace(ch, '')
        else:
            continue
    title = title.replace(' ', '_')
    return title


def get_req(link, page):
    res = requests.get('https://www.nature.com' + link + page)
    print('https://www.nature.com' + link + page)
    if res.status_code == 200:
        # print('200')
        return res
    else:
        print('\n' + 'The URL returned ' + str(res.status_code) + '!')


n_pages = int(input())
category = str(input())
lst_title = []
lst_category = []
lst_of_p = []
f_t = ''

for i in range(n_pages):
    os.chdir(r'C:\Users\Ant\PycharmProjects\Web Scraper\Web Scraper\task')
    if not os.access(r'C:\Users\Ant\PycharmProjects\Web Scraper\Web Scraper\task\Page_' + str(i + 1), os.F_OK):
        os.mkdir('Page_' + str(i + 1))
    else:
        os.rmdir('Page_' + str(i + 1))
        os.mkdir('Page_' + str(i + 1))

    req = get_req('/nature/articles/?searchType=journalSearch&sort=PubDate&page=', str(i + 1))
    sup = BeautifulSoup(req.content, 'html.parser')
    lst_title = sup.find_all('a', class_='c-card__link u-link-inherit', )
    lst_category = sup.find_all('span', class_='c-meta__type')

    for j in range(len(lst_title)):
        if lst_category[j].text.strip(' ') == category:
            link = lst_title[j].get('href')
            # print(link)
            art_type = get_req(link, '')
            bs = BeautifulSoup(art_type.content, 'html.parser')
            f_t = format_title(lst_title[j].text.strip(' '))
            letter_body = bs.find_all('div', class_='article-item__body')
            # print(letter_body)
            # print(bs.content)
            with open(r'C:\Users\Ant\PycharmProjects\Web Scraper\Web Scraper\task\Page_'
                      + str(i + 1) + '/' + f_t + '.txt', 'wb') as f:
                for b in letter_body:
                    print(b)
                    f.write((bytes(b.text.replace('\n', ''), encoding='utf8')))
                f.close()

        else:
            continue
# Research Highlight
