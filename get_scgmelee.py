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


melee = "https://mtgmelee.com/Organization/View/530"


target_url = 'https://mtgmelee.com/Organization/View/530'

# target_html = requests.get(target_url).text
# root = lxml.html.fromstring(target_html)
# #text_content()メソッドはそのタグ以下にあるすべてのテキストを取得する
# root.cssselect('#past-results-table >tbody>tbody').text_content()

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