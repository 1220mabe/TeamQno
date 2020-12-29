# coding: UTF-8
print("---------------Start getting MTG Melee TournamentList------------------")

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

formatlist = ['Standard', 'Historic','Pioneer']

def get_tournamentlist(deck_url):
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

    #print(tbody)
    urllist = []
    tbody = soup.select(".odd")
    #開催大会ループ 奇数
    for trow in tbody:
        decklists = trow.find('td', class_='Decklists-column').text
        if int(decklists) >= 20:
            format = trow.find('td', class_='Format-column').text
            if format in formatlist:
                #URL作成
                url = trow.find('a')
                # getでリンク要素のhref属性の値を取得して出力
                print(url.get('href'))
                urllist.append(u'https://mtgmelee.com/' + url.get('href'))

    tbody = soup.select(".even")

    #開催大会ループ 偶数
    for trow in tbody:
        decklists = trow.find('td', class_='Decklists-column').text
        if int(decklists) >= 20:
            format = trow.find('td', class_='Format-column').text
            if format in formatlist:
                #URL作成
                url = trow.find('a')
                # getでリンク要素のhref属性の値を取得して出力
                print(url.get('href'))
                urllist.append(u'https://mtgmelee.com/' + url.get('href'))

    # ドライバーを終了させる
    driver.close()
    driver.quit()
    urllist.reverse()
    #print(urllist)
    return(urllist)

        #<tbody>
        #<tr class="even" role="row">
        #<td class="StartDate-column sorting_1">Last Saturday at 10:00 AM JST</td>
        #<td class="Name-column"><a href="/Tournament/View/4481#standings">日本選手権2020冬　本戦</a></td>
        #<td class="OrganizationName-column"><a href="/Organization/View/678">BIG MAGIC</a></td>
        #<td class="Format-column">Historic</td>
        #<td class="Decklists-column"><a href="/Tournament/View/4481#standings">126</a></td>
        #</tr>
        #</tbody>

# URL引数で1デッキはアップロード可能
#get_list(r'https://mtgmelee.com/Tournaments')


print("---------------End getting MTG Melee TournamentList--------------------")
