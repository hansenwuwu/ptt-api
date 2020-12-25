import json
import requests
from bs4 import BeautifulSoup
import os
import datetime

t = datetime.datetime.now()

PTT_URL = 'https://www.ptt.cc'

content = requests.get(
            url= 'https://www.ptt.cc/bbs/' + 'LOL' + '/index.html',
            cookies={'over18': '1'}, timeout=3
        ).content.decode('utf-8')

# f = open('test.html', 'a')
# f.write(content)
# f.close()

soup = BeautifulSoup(content, 'html.parser')

'''
找出上下頁
'''
# action_bar_container = soup.find('div', {'id': 'action-bar-container'})
# links = action_bar_container.find_all('a')
# for a in links:
#     if "上頁" in a.text:
#         print(a)


divs = soup.find_all("div", "r-ent")
for div in divs:
    try:
        # ex. link would be <a href="/bbs/PublicServan/M.1127742013.A.240.html">Re: [問題] 職等</a>

        author = "null"
        article_name = "null"
        push = "null"
        href = "null"
        mark = "null"

        # mark 標示這個文章是否置頂或是公告
        if div.find('div', 'author'):
            author = div.find('div', 'author').text
        if div.find('a'):
            article_name = div.find('a').text

        # 文章預覽
        if div.find('div', 'nrec'):
            push = div.find('div', 'nrec').text

        # 文章回應數
        if div.find('a'):
            href = div.find('a')['href']
        if div.find('div', 'mark'):
            mark = div.find('div', 'mark').text

        print(article_name, ' mark: ',mark, ': ', href, ', ', push, '\n')

        '''
        parse each page
        all push  拿總回應數會花很多時間
        '''
        # article = requests.get(
        #     url= 'https://www.ptt.cc' + href,
        #     cookies={'over18': '1'}, timeout=3
        # ).content.decode('utf-8')

        # article_soup = BeautifulSoup(article, 'html.parser')
        # main_content = article_soup.find('div', {"id": 'main-content'})

        # # 
        # pushes = main_content.find_all('div', 'push')
        # # print( len(pushes) )

    except Exception as e:
        print(e)

print( (datetime.datetime.now() - t) )
