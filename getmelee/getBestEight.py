# coding: UTF-8
print("---------------Start getting MTG Melee DeckList------------------")

import requests
import urllib
import chromedriver_binary
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mo = "https://magic.wizards.com/en/articles/archive/mtgo-standings/"

def get_meleedecklist(deck_url):
    # ブラウザのオプションを格納する変数をもらってきます。
    options = Options()
    # Headlessモードを有効にする（コメントアウトするとブラウザが実際に立ち上がります）
    options.set_headless(True)
    # ブラウザを起動する
    driver = webdriver.Chrome()
    # ブラウザでアクセスする
    driver.get(deck_url)
    # HTMLを文字コードをUTF-8に変換してから取得します。
    deck_url = driver.page_source.encode('utf-8')

    # URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます

    soup = BeautifulSoup(deck_url, "html.parser")
    #print(soup)
    #print(tbody)
    urllist = []
    tbody = soup.select(".odd")
    #開催大会ループ 1位
    for trow in tbody:
        if trow.find('td', class_='Rank-column sorting_1'):
            rank = trow.find('td', class_='Rank-column sorting_1').text
            if rank == '1':
                #URL作成
                if trow.find('td', class_='Decklists-column'):
                    column = trow.find('td', class_='Decklists-column')
                    a = column.find('a')
                    # getでリンク要素のhref属性の値を取得して出力
                    print(u'https://mtgmelee.com' + a.attrs['href'])
                    urllist.append(u'https://mtgmelee.com' + a.attrs['href'])
                    break

    tbody = soup.select(".even")
    #開催大会ループ 2位
    for trow in tbody:
        if trow.find('td', class_='Rank-column sorting_1'):
            rank = trow.find('td', class_='Rank-column sorting_1').text
            if rank == '2':
                #URL作成
                if trow.find('td', class_='Decklists-column'):
                    column = trow.find('td', class_='Decklists-column')
                    a = column.find('a')
                    # getでリンク要素のhref属性の値を取得して出力
                    print(u'https://mtgmelee.com' + a.attrs['href'])
                    urllist.append(u'https://mtgmelee.com' + a.attrs['href'])
                    break

    #開催大会ループ 3位
    tbody = soup.select(".odd")
    for trow in tbody:
        if trow.find('td', class_='Rank-column sorting_1'):
            rank = trow.find('td', class_='Rank-column sorting_1').text
            if rank == '3':
                #URL作成
                if trow.find('td', class_='Decklists-column'):
                    column = trow.find('td', class_='Decklists-column')
                    a = column.find('a')
                    # getでリンク要素のhref属性の値を取得して出力
                    print(u'https://mtgmelee.com' + a.attrs['href'])
                    urllist.append(u'https://mtgmelee.com' + a.attrs['href'])
                    break

    #開催大会ループ 4位
    tbody = soup.select(".even")
    for trow in tbody:
        if trow.find('td', class_='Rank-column sorting_1'):
            rank = trow.find('td', class_='Rank-column sorting_1').text
            if rank == '4':
                #URL作成
                if trow.find('td', class_='Decklists-column'):
                    column = trow.find('td', class_='Decklists-column')
                    a = column.find('a')
                    # getでリンク要素のhref属性の値を取得して出力
                    print(u'https://mtgmelee.com' + a.attrs['href'])
                    urllist.append(u'https://mtgmelee.com' + a.attrs['href'])
                    break

    #開催大会ループ 5位
    tbody = soup.select(".odd")
    for trow in tbody:
        if trow.find('td', class_='Rank-column sorting_1'):
            rank = trow.find('td', class_='Rank-column sorting_1').text
            if rank == '5':
                #URL作成
                if trow.find('td', class_='Decklists-column'):
                    column = trow.find('td', class_='Decklists-column')
                    a = column.find('a')
                    # getでリンク要素のhref属性の値を取得して出力
                    print(u'https://mtgmelee.com' + a.attrs['href'])
                    urllist.append(u'https://mtgmelee.com' + a.attrs['href'])
                    break

    #開催大会ループ 6位
    tbody = soup.select(".even")
    for trow in tbody:
        if trow.find('td', class_='Rank-column sorting_1'):
            rank = trow.find('td', class_='Rank-column sorting_1').text
            if rank == '6':
                #URL作成
                if trow.find('td', class_='Decklists-column'):
                    column = trow.find('td', class_='Decklists-column')
                    a = column.find('a')
                    # getでリンク要素のhref属性の値を取得して出力
                    print(u'https://mtgmelee.com' + a.attrs['href'])
                    urllist.append(u'https://mtgmelee.com' + a.attrs['href'])
                    break

    #開催大会ループ 7位
    tbody = soup.select(".odd")
    for trow in tbody:
        if trow.find('td', class_='Rank-column sorting_1'):
            rank = trow.find('td', class_='Rank-column sorting_1').text
            if rank == '7':
                #URL作成
                if trow.find('td', class_='Decklists-column'):
                    column = trow.find('td', class_='Decklists-column')
                    a = column.find('a')
                    # getでリンク要素のhref属性の値を取得して出力
                    print(u'https://mtgmelee.com' + a.attrs['href'])
                    urllist.append(u'https://mtgmelee.com' + a.attrs['href'])
                    break

    #開催大会ループ 8位
    tbody = soup.select(".even")
    for trow in tbody:
        if trow.find('td', class_='Rank-column sorting_1'):
            rank = trow.find('td', class_='Rank-column sorting_1').text
            if rank == '8':
                #URL作成
                if trow.find('td', class_='Decklists-column'):
                    column = trow.find('td', class_='Decklists-column')
                    a = column.find('a')
                    # getでリンク要素のhref属性の値を取得して出力
                    print(u'https://mtgmelee.com' + a.attrs['href'])
                    urllist.append(u'https://mtgmelee.com' + a.attrs['href'])
                    break


    # ドライバーを終了させる
    driver.close()
    driver.quit()
    urllist.reverse()
    #print(urllist)
    return urllist

# <tr class="odd" role="row">
# <td class="Rank-column sorting_1">1</td><td class="Name-column">
# <a class="mr-1" data-id="115390" data-toggle="hovercard" data-type="player" href="/Profile/Index/SIN">Masashiro Kuroda
# <svg aria-hidden="true" class="svg-inline--fa fa-info-circle fa-w-16 fa-fw" data-fa-i2svg="" data-icon="info-circle" data-prefix="fas" focusable="false" role="img" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
# <path d="M256 8C119.043 8 8 119.083 8 256c0 136.997 111.043 248 248 248s248-111.003 248-248C504 119.083 392.957 8 256 8zm0 110c23.196 0 42 18.804 42 42s-18.804 42-42 42-42-18.804-42-42 18.804-42 42-42zm56 254c0 6.627-5.373 12-12 12h-88c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h12v-64h-12c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h64c6.627 0 12 5.373 12 12v100h12c6.627 0 12 5.373 12 12v24z" fill="currentColor"></path></svg>
# <!-- <i class="fas fa-info-circle fa-fw"></i> --></a>
# <a class="text-twitter mr-1" href="https://twitter.com/@masashiro41236" target="_blank">
# <svg aria-hidden="true" class="svg-inline--fa fa-twitter fa-w-16" data-fa-i2svg="" data-icon="twitter" data-prefix="fab" focusable="false" role="img" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg">
# <path d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z" fill="currentColor"></path>
# </svg><!-- <img class="fab fa-twitter"> --></a></td>
# <td class="Decklists-column">
# <a data-id="88147" data-toggle="hovercard" data-type="decklist" href="/Decklist/View/88147">Sultai Midrange <svg aria-hidden="true" class="svg-inline--fa fa-info-circle fa-w-16 fa-fw" data-fa-i2svg="" data-icon="info-circle" data-prefix="fas" focusable="false" role="img" viewbox="0 0 512 512" xmlns="http://www.w3.org/2000/svg"><path d="M256 8C119.043 8 8 119.083 8 256c0 136.997 111.043 248 248 248s248-111.003 248-248C504 119.083 392.957 8 256 8zm0 110c23.196 0 42 18.804 42 42s-18.804 42-42 42-42-18.804-42-42 18.804-42 42-42zm56 254c0 6.627-5.373 12-12 12h-88c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h12v-64h-12c-6.627 0-12-5.373-12-12v-24c0-6.627 5.373-12 12-12h64c6.627 0 12 5.373 12 12v100h12c6.627 0 12 5.373 12 12v24z" fill="currentColor"></path></svg><!--
# <i class="fas fa-info-circle fa-fw"></i> --></a></td><td class="Record-column">10-2-0</td><td class="Points-column">N/A</td><td class="Tiebreaker1-column">N/A</td><td class="Tiebreaker2-column">N/A</td>
# <td class="Tiebreaker3-column">N/A</td>
# </tr>

# URL引数で1デッキはアップロード可能
#get_list(r'https://mtgmelee.com/Tournament/View/4481#standings')


print("---------------End getting MTG Melee DeckList--------------------")
