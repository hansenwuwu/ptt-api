# uvicorn main:app --reload
import uvicorn
from fastapi import FastAPI

import json
import requests
from bs4 import BeautifulSoup

app = FastAPI()

PTT_URL = 'https://www.ptt.cc'

@app.get('/')
@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/forum/popular")
async def popular_forum():
    content = requests.get(
            url= PTT_URL + '/bbs/index.html',
            cookies={'over18': '1'}, timeout=3
        ).content.decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')

    boards = soup.find_all("div", "b-ent")
    output = []
    count = 0
    for board in boards:
        if count >= 20:
            break
        count += 1
        m = {}
        # m['board_name'] = ""
        # m['board_nuser'] = 0
        a = board.find('a', 'board')
        if a.find('div', "board-name"):
            m['board_name'] = a.find('div', "board-name").text
        if a.find('div', 'board-nuser').find('span', 'hl'):
            m['board_nuser'] = a.find('div', 'board-nuser').find('span', 'hl').text
        output.append(m)
    # output = json.dumps(output)
    return {"message": output}

@app.get("/api/v1/forum/{forum_name}")
async def forum_(forum_name, page: int = 0):
    content = requests.get(
            url= PTT_URL + '/bbs/' + forum_name + '/index.html',
            cookies={'over18': '1'}, timeout=3
        ).content.decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    divs = soup.find_all("div", "r-ent")
    articles = []
    for div in divs:
        m = {}
        m['author'] = "null"
        m['article_name'] = "null"
        m['push'] = "null"
        m['href'] = "null"
        m['mark'] = "null"
        try:
            # ex. link would be <a href="/bbs/PublicServan/M.1127742013.A.240.html">Re: [問題] 職等</a>

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
        articles.append(m)

    return {"forum": forum_name, "page": page, "articles": articles}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)