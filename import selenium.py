import selenium
from selenium import webdriver
import time
import os
import requests
import csv
import re
import post_article
import output_graph
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from urllib.request import urlopen
from collections import Counter
from collections import OrderedDict
from datetime import date,timedelta

browser = webdriver.Chrome()
browser.maximize_window() #画面サイズを最大化
login_url = "https://teamqno.work/wp-login.php" #あなたのブログのログインページを設定してください
browser.get(login_url)
time.sleep(1)

#ログイン処理
username = ""
password = ""

elem_username = browser.find_element_by_id("user_login")
elem_username.send_keys(username)
time.sleep(1)

elem_password = browser.find_element_by_id("user_pass")
elem_password.send_keys(password)
time.sleep(1)

browser.find_element_by_id("wp-submit").click()
time.sleep(1)

#値を入れる箱をつくる
ids = []

for i in range(7): #何回繰り返すかは取得する記事の数次第
    # アクセス先のURL
    url = "https://teamqno.work/wp-admin/edit-tags.php?taxonomy=post_tag&paged={}".format(i+1)
    browser.get(url)

     #タイトル取得
    elems_post_title = browser.find_element_by_tag_name("input")
    print(elems_post_title[value])


print(ids)
