import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import sys
# import os

req = requests.get("http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf")
html = req.text
bsObj = BeautifulSoup(html, "html.parser")
book_page_urls = [a.attrs.get('href') for a in bsObj.select('div.title a[href^="http://www.kyobobook.co.kr/product/detailViewKor.laf"]')]


f = open("result.txt","a", encoding="utf-8")


# print(book_page_urls)
with open("result.txt", "a", encoding="utf-8") as f:
    for book_page_url in book_page_urls:
        req = requests.get(book_page_url)
        bsObj = BeautifulSoup(req.text, "html.parser")
        title = bsObj.select( "h1.title strong" )[0].get_text().strip()
        author = bsObj.select( "span.name  a" )[0].get_text()
        # print (title + " / " + "저자:" + author)
        data = (title + " / " + "저자:" + author)
        f.write(data)
