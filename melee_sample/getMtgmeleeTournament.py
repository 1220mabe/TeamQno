# coding: UTF-8
print("---------------Start getting MTG Melee List------------------")

import requests
import urllib
import chromedriver_binary
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mo = "https://magic.wizards.com/en/articles/archive/mtgo-standings/"

categorystan = "Standard"
categoryhist = "Historic"
categorypio = "Pioneer"

csvfile = ".csv"
txtfile = ".txt"
DeckPath = "E:\\TeamQno\\Decks\\"

def get_list(deck_url):
    # ブラウザのオプションを格納する変数をもらってきます。
    options = Options()
    # Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
    options.set_headless(True)
    # ブラウザを起動する
    driver = webdriver.Chrome(executable_path='/Users/masaruabe/Downloads/chromedriver')
    # ブラウザでアクセスする
    driver.get(deck_url)
    # HTMLを文字コードをUTF-8に変換してから取得します。
    deck_url = driver.page_source.encode('utf-8')

    # URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
    soup = BeautifulSoup(deck_url, "html.parser")
    print(soup)

    #MTGAテキスト
    #deck_arena = soup.find('textarea', class_='decklist-builder-copy-field form-control mt-2')

    #プレイヤー名
    #player_name = soup.find('span', class_='decklist-card-title-author')
    #print(player_name.text.replace('by ', ''))
    #フォーマット
    #forma  = soup.findAll('div', class_='decklist-card-info mr-3')
    #category = forma[1].text.strip()
    #print(category)
    #大会名
    #tournament_name = soup.find('div', class_='decklist-card-info-tournament mr-3')
    #print(tournament_name.text.strip())

# URL引数で1デッキはアップロード可能
get_list(r'https://mtgmelee.com/Tournament/Search?formats=Standard,Historic,Pioneer&date=Last7Days')

print("---------------End getting MTG Melee List--------------------")
