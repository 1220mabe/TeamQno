print("---------------Start getting MTG Melee List------------------")

import os
import requests
import csv
import re
import categorize_decks
import post_article
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import time

today =  datetime.today()
yesterday = today - timedelta(days=1)
dbyesterday = today - timedelta(days=2)
tdyesterday = today - timedelta(days=3)

mo = "https://magic.wizards.com/en/articles/archive/mtgo-standings/"

categorystan = "Standard"
categoryhist = "Historic"
categorypio = "Pioneer"

csvfile = ".csv"
txtfile = ".txt"
DeckPath = "E:\\TeamQno\\Decks\\"

def make_row(count, name,decklist):
    card_count = str(count.text)
    card_name = str(name.text)
    row = []
    row.append("<span style=\"font-size: 14px;\">" + card_count)
    row.append(card_name + "</span>")
    row_str=' '.join(row)
    decklist.append(row_str)
    return

def get_and_postlist(deck_url):
    r = requests.get(deck_url)
    soup = BeautifulSoup(r.content, "html.parser")

    #MTGAテキスト
    deck_arena = soup.find('textarea', class_='decklist-builder-copy-field form-control mt-2')

    #プレイヤー名
    player_name = soup.find('span', class_='decklist-card-title-author')
    print(player_name.text.replace('by ', ''))
    #フォーマット
    forma  = soup.findAll('div', class_='decklist-card-info mr-3')
    category = forma[1].text.strip()
    print(category)
    #大会名
    tournament_name = soup.find('div', class_='decklist-card-info-tournament mr-3')
    print(tournament_name.text.strip())

    #デッキリスト作成
    deck = []
    deck.append("<center>")
    deck.append("<b>" + tournament_name.text.strip()+"</b>")
    deck.append("<b>" + player_name.text.replace('by ', '') + "</b>")
    deck.append("[mtg_deck]")

    #ラベル
    kinds = soup.findAll('table', class_='decklist-section-table full-width')
    for kind in kinds:
        labels = kind.findAll('td', class_='decklist-builder-section-label-cell')
        for label in labels:
            #プレインズウォーカー
            if label.text =='Planeswalker':
                deck.append('<span style=\"font-size: 14px;\"><b>Planeswalker</b></span>')
                card_count = kind.findAll('td', class_='decklist-builder-card-quantity-cell')
                card_name = kind.findAll('td', class_='decklist-builder-card-name-cell')
                for i in range(len(card_count)):
                    make_row(card_count[i], card_name[i], deck)
            #クリーチャー
            if label.text =='Creature':
                deck.append('<span style=\"font-size: 14px;\"><b>Creature</b></span>')
                card_count = kind.findAll('td', class_='decklist-builder-card-quantity-cell')
                card_name = kind.findAll('td', class_='decklist-builder-card-name-cell')
                for i in range(len(card_count)):
                    make_row(card_count[i], card_name[i], deck)
            #アーティファクト
            if label.text =='Artifact':
                deck.append('<span style=\"font-size: 14px;\"><b>Artifact</b></span>')
                card_count = kind.findAll('td', class_='decklist-builder-card-quantity-cell')
                card_name = kind.findAll('td', class_='decklist-builder-card-name-cell')
                for i in range(len(card_count)):
                    make_row(card_count[i], card_name[i], deck)
            #エンチャント
            if label.text =='Enchantment':
                deck.append('<span style=\"font-size: 14px;\"><b>Enchantment</b></span>')
                card_count = kind.findAll('td', class_='decklist-builder-card-quantity-cell')
                card_name = kind.findAll('td', class_='decklist-builder-card-name-cell')
                for i in range(len(card_count)):
                    make_row(card_count[i], card_name[i], deck)
            #ソーサリー
            if label.text =='Sorcery':
                deck.append('<span style=\"font-size: 14px;\"><b>Sorcery</b></span>')
                card_count = kind.findAll('td', class_='decklist-builder-card-quantity-cell')
                card_name = kind.findAll('td', class_='decklist-builder-card-name-cell')
                for i in range(len(card_count)):
                    make_row(card_count[i], card_name[i], deck)
            #インスタント
            if label.text =='Instant':
                deck.append('<span style=\"font-size: 14px;\"><b>Instant</b></span>')
                card_count = kind.findAll('td', class_='decklist-builder-card-quantity-cell')
                card_name = kind.findAll('td', class_='decklist-builder-card-name-cell')
                for i in range(len(card_count)):
                    make_row(card_count[i], card_name[i], deck)
            #ランド
            if label.text =='Land':
                deck.append('<span style=\"font-size: 14px;\"><b>Land</b></span>')
                card_count = kind.findAll('td', class_='decklist-builder-card-quantity-cell')
                card_name = kind.findAll('td', class_='decklist-builder-card-name-cell')
                for i in range(len(card_count)):
                    make_row(card_count[i], card_name[i], deck)
            #サイドボード
            if label.text =='Sideboard':
                deck.append('<span style=\"font-size: 14px;\"><b>Sideboard</b></span>')
                card_count = kind.findAll('td', class_='decklist-builder-card-quantity-cell')
                card_name = kind.findAll('td', class_='decklist-builder-card-name-cell')
                for i in range(len(card_count)):
                    make_row(card_count[i], card_name[i], deck)
    deck.append("[/mtg_deck]")

    # MTGAtxtファイル存在チェック(ここでポスト判定)
    txtfile= (tournament_name.text.strip() +" " + player_name.text.replace('by ', '') + ".txt").replace(' ', '-').replace('(', '').replace(')', '')
    txtfile= txtfile.replace('#','-')
    txtfile= txtfile.replace('---','-')
    txtfile= txtfile.replace('--','-')
    if os.path.exists(DeckPath + txtfile) and os.path.getsize(DeckPath +txtfile) > 0:
        return
    # MTGACode Botton作成
    today_str = datetime.today().strftime('%Y/%m/')
    mtgacode_url = ("https://teamqno.work/wp-content/uploads/"+ today_str + txtfile)
    mtgacode_botton = ("[maxbutton id=\"9\" url=\"%s\"]"  % mtgacode_url)
    deck.append(mtgacode_botton)
    deck.append("</center>")
    print(deck)

    #アーキタイプカテゴライズ
    results =[2]
    if category == categorystan:
        category_list = [15,34]
        results = categorize_decks.check_arc_stan(deck)
    if category == categoryhist:
        category_list = [15,35]
        results = categorize_decks.check_arc_hist(deck)
    if category == categorypio:
        category_list = [15,36]
        results = categorize_decks.check_arc_pion(deck)
    post_title = results[0]
    media_id = results[1]

    #タグID作成
    post_article.post_tag(tournament_name.text.strip())
    #タグID取得
    title_list = []
    title_list.append(int(post_article.get_tags()))
    #ポスト(投稿)
    post_article.post_article('publish',post_title,post_title,'\r\n\r\n'.join(deck),category_list,title_list,media_id)

    # MTGAtxtファイル追記
    with open(DeckPath + txtfile, mode='w') as f:
        f.writelines(deck_arena.replace('\n',''))
    # MTGAtxtファイルクローズド
    f.close()
    # MTGAtxtファイルアップロード
    post_article.post_txt(DeckPath+txtfile)
    if os.path.getsize(DeckPath + txtfile) <= 0:
        os.remove(DeckPath + txtfile)

# URL引数で1デッキはアップロード可能
#get_list(r'https://mtgmelee.com/Decklist/View/87420')


# デッキリストポストとcsv作成
# https://mtgmelee.com/Decklist/View/34981

print("---------------End getting MTG Melee List--------------------")
