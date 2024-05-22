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

url = "https://www.wanplus.cn/lol/teamstats"
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
                "战队": row_data[1],
                "KDA": row_data[2],
                "场均击杀": row_data[3],
                "场均死亡": row_data[4],
                "每分钟伤害": row_data[5],
                "一血率": row_data[6],
                "场均时长": row_data[7],
                "场均经济": row_data[8],
                "每分钟经济": row_data[9],
                "每分钟补刀": row_data[10],
            }

            )
    return data


# rows = scrapy(url, headers)
# data = []
# data = cut(rows)
# print(data)
# with open(r'LOL.txt', 'w') as f:
#     for i in data:
#         f.write(str(i) + '\n')


def get_proxy():
    PROXY_POOL_URL = 'http://localhost:5555/random'
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


print(get_proxy())
