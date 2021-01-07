import json
import requests
from bs4 import BeautifulSoup
import os
import datetime

PTT_URL = 'https://www.ptt.cc'

FORUM = 'Gossiping'

content = requests.get(
            url= PTT_URL + '/bbs/' + FORUM + '/index.html',
            cookies={'over18': '1'}, timeout=3
        ).content.decode('utf-8')
soup = BeautifulSoup(content, 'html.parser')
divs = soup.find_all("div", {"class": ["r-ent", 'r-list-sep']}, )

posts = []

for div in divs:
    try:
        # ex. link would be <a href="/bbs/PublicServan/M.1127742013.A.240.html">Re: [問題] 職等</a>
        if div['class'][0] == "r-list-sep":
            print('it is a seperate, means after this div is always top')
            break

        m = {}
        m['author'] = ''
        m['article_name'] = ''
        m['push'] = ''
        m['href'] = ''
        m['mark'] = ''

        # mark 標示這個文章是否置頂或是公告
        if div.find('div', 'author'):
            m['author'] = div.find('div', 'author').text
        if div.find('a'):
            m['article_name'] = div.find('a').text

        # 文章預覽
        if div.find('div', 'nrec'):
            m['push'] = div.find('div', 'nrec').text

        # 文章回應數
        if div.find('a'):
            m['href'] = div.find('a')['href']
        if div.find('div', 'mark'):
            m['mark'] = div.find('div', 'mark').text

        posts.append(m)

        # print(m['article_name'], ' mark: ', m['mark'], ': ', m['href'], ', ', m['push'], '\n')
    except Exception as e:
        print(e)
    
posts.reverse()
print(posts)