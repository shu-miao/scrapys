import re
import urllib.error
import urllib.request
import requests
import xlwt
from bs4 import BeautifulSoup
import lxml
import csv
import pandas
import numpy
from openpyxl import load_workbook

url = "https://wanplus.cn/lol/playerstats"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
                  'Safari/537.36'}


def scrapy(url, headers):
    strhtml = requests.get(url, headers=headers)
    soup = BeautifulSoup(strhtml.text, 'lxml')
    # print(soup)
    info = soup.find('tbody')
    rows = info.find_all('tr')
    return rows


def cut(rows):
    data = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) > 1:
            row_data = [cell.text.strip() for cell in cells]
            data.append({
                "名次": row_data[0],
                "选手": row_data[1],
                "战队": row_data[2],
                "位置": row_data[3],
                "出场次数": row_data[4],
                "KDA": row_data[5],
                "参团率": row_data[6],
                "场均击杀": row_data[7],
                "单场最高击杀": row_data[8],
                "场均死亡": row_data[9],
                "单场最高死亡": row_data[10],
                "场均助攻": row_data[11],
            }

            )
    return data


rows = scrapy(url, headers)
data = []
data = cut(rows)
print(data)
with open(r'LOL_players.txt', 'w') as f:
    for i in data:
        f.write(str(i) + '\n')
