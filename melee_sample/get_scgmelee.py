import os
import requests
import csv
import re
import categorize_decks
import post_article
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from urllib.request import urlopen
import lxml.html
from selenium import webdriver
from requests_html import HTMLSession


melee = "https://mtgmelee.com/Tournament/View/2402#standings"

# target_html = requests.get(target_url).text
# root = lxml.html.fromstring(target_html)
# #text_content()メソッドはそのタグ以下にあるすべてのテキストを取得する
# root.cssselect('#past-results-table >tbody>tbody').text_content()

browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.get("https://mtgmelee.com/Tournament/Search?formats=Standard,Pioneer,Historic&date=Last7Days")

for i in range(10):
    # 3秒ごとに取得
    #time.sleep(3)
    bc_value = browser.find_element_by_id("svg-inline--fa fa-user fa-w-14 mr-1").text
    print(bc_value)

# セッション開始
session = HTMLSession()
r = session.get(melee)

# ブラウザエンジンでHTMLを生成させる
r.html.render()

# スクレイピング
ranking_rows = r.html.find('#past-results-table,tbody,a')
ranking_list = []
if ranking_rows:
    print(ranking_rows)

    # 1〜5位だけを取得
    ranking_top5 = ranking_rows[0].find("p.que_3")
    for item in ranking_top5:
        ranking_list.append(item.text[2:])

print(ranking_list)
