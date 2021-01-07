from fastapi import fastapi

import json
import requests
from bs4 import BeautifulSoup

app = FastAPI()

PTT_URL = 'https://www.ptt.cc'

@app.get('/')
@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/popular-forum")
async def popular_forum():
    content = requests.get(
            url= PTT_URL + '/bbs/index.html',
            cookies={'over18': '1'}, timeout=3
        ).content.decode('utf-8')
    soup = BeautifulSoup(content, 'html.parser')
    
    return {"message": "Hello World"}
