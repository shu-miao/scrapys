import re
import urllib.error
import urllib.request
import requests
import xlwt
from bs4 import BeautifulSoup
import lxml

url = "https://bbs.oldmantvg.net/index-1.htm"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
strhtml = requests.get(url, headers=headers)
soup = BeautifulSoup(strhtml.text, 'lxml')
# print(strhtml.text)
# print(soup)
info = soup.select('.media-body')
A,B = 'htm">','</a>'
# print(A,B)
temp = re.findall(f"{A}.+?{B}",str(info))
result = re.sub(f"{A}|{B}","",str(temp))
C,D,E = '<span class="huux_thread_hlight_style1">','<span class="huux_thread_hlight_style2">','</span>'
result0 = re.sub(f"{C}|{D}|{E}","",str(result))
# print(info)
print(result0)
