import json
import requests
from bs4 import BeautifulSoup
import os
import datetime

PTT_URL = 'https://www.ptt.cc'
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
    m['board_name'] = ""
    m['board_nuser'] = 0
    a = board.find('a', 'board')
    if a.find('div', "board-name"):
        m['board_name'] = a.find('div', "board-name").text
    if a.find('div', 'board-nuser').find('span', 'hl'):
        m['board_nuser'] = a.find('div', 'board-nuser').find('span', 'hl').text
    output.append(m)
print(output)