print("Hello World")

import os
import requests
import csv
import re
import categorize_decks
import post_article
from datetime import datetime, date, timedelta
from bs4 import BeautifulSoup
from urllib.request import urlopen

today =  datetime.today()
yesterday = today - timedelta(days=1)
dbyesterday = today - timedelta(days=2)
tdyesterday = today - timedelta(days=3)

mo = "https://magic.wizards.com/en/articles/archive/mtgo-standings/"
stdlea = "Standard-League"
stdcha = "Standard-Challenge"
stdpre = "Standard-Preliminary"
piolea = "Pioneer-League"
piocha = "Pioneer-Challenge"
piopre = "Pioneer-Preliminary"
categorystan = "Decks,Standard"
categorypio = "Decks,Pioneer"

csvfile = ".csv"
txtfile = ".txt"
DeckPath = "E:\\TeamQno\\Decks\\"

def make_row(span_row_list, decks):
    for span_row in span_row_list:
        row = []
        card_count_r = span_row.find("span",{"class":"card-count"})
        card_name_r = span_row.find("span",{"class":"card-name"})
        card_count = str(card_count_r.text)
        card_name = str(card_name_r.text)
        row.append("<span style=\"font-size: 14px;\">" + card_count)
        row.append(card_name + "</span>")
        row_str=' '.join(row)
        decks.append(row_str)
    return

def make_row_simple(span_row_list, decks):
    for span_row in span_row_list:
        row = []
        card_count_r = span_row.find("span",{"class":"card-count"})
        card_name_r = span_row.find("span",{"class":"card-name"})
        card_count = str(card_count_r.text)
        card_name = str(card_name_r.text)
        row.append("\n" + card_count)
        row.append(card_name)
        row_str=' '.join(row)
        decks.append(row_str)
    return

#MOデッキリストをcsvファイル化
def to_csv_mo(url, filename,filename_,title,category):

    csvheader_data = []
    # ファイルヘッダー挿入
    csvheader_data.append('post_id')
    csvheader_data.append('post_name')
    csvheader_data.append('post_author')
    csvheader_data.append('post_date')
    csvheader_data.append('post_type')
    csvheader_data.append('post_status')
    csvheader_data.append('post_thumbnail')
    csvheader_data.append('post_title')
    csvheader_data.append('post_content')
    csvheader_data.append('post_category')
    csvheader_data.append('post_tags')
    csvheader_data.append('custom_field')
    csvheader_data.append('custom_field')
    csvheader_data.append('post_thumbnail')

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    players = soup.select('.content.beanSpacing')

    for player in players:
        final_csv_data = []
        csv_data=[]
        decks = []
        decks_arena = []
        player_name = player.find("h4")
        # ファイル存在チェック
        if os.path.exists(filename + " " + player_name.text + csvfile) and os.path.getsize(filename + " " + player_name.text + csvfile) > 0:
            return
        # ファイルオープン
        csv_file = open(filename + " " + player_name.text + csvfile, 'wt', newline = '', encoding = 'utf-8')
        csv_write = csv.writer(csv_file)
        
        decks.append("<b>" + title +"</b>")
        decks.append("<b>" + player_name.text + "</b>")
        decks.append("[mtg_deck]")
        decks_arena.append("Deck")
        #プレインズウォーカー
        planeswalkers = player.find('div', class_='sorted-by-planeswalker clearfix element')
        if planeswalkers:
            decks.append("<span style=\"font-size: 14px;\"><b>Planeswalker</b></span>")
            span_row_list = planeswalkers.findAll("span",{"class":"row"})
            make_row(span_row_list, decks)
            make_row_simple(span_row_list, decks_arena)
        #クリーチャー
        creatures = player.find('div', class_='sorted-by-creature clearfix element')
        if creatures:
            decks.append("<span style=\"font-size: 14px;\"><b>Creature</b></span>")
            span_row_list = creatures.findAll("span",{"class":"row"})
            make_row(span_row_list, decks)
            make_row_simple(span_row_list, decks_arena)
        #インスタント
        instants = player.find('div', class_='sorted-by-instant clearfix element')
        if instants:
            decks.append("<span style=\"font-size: 14px;\"><b>Instant</b></span>")
            span_row_list = instants.findAll("span",{"class":"row"})
            make_row(span_row_list, decks)
            make_row_simple(span_row_list, decks_arena)
        #ソーサリー
        sorcerys = player.find('div', class_='sorted-by-sorcery clearfix element')
        if sorcerys:
            decks.append("<span style=\"font-size: 14px;\"><b>Sorcery</b></span>")
            span_row_list = sorcerys.findAll("span",{"class":"row"})
            make_row(span_row_list, decks)
            make_row_simple(span_row_list, decks_arena)
        #エンチャント
        enchantments = player.find('div', class_='sorted-by-enchantment clearfix element')
        if enchantments:
            decks.append("<span style=\"font-size: 14px;\"><b>Enchantment</b></span>")
            span_row_list = enchantments.findAll("span",{"class":"row"})
            make_row(span_row_list, decks)
            make_row_simple(span_row_list, decks_arena)
        #アーティファクト
        artifacts = player.find('div', class_='sorted-by-artifact clearfix element')
        if artifacts:
            decks.append("<span style=\"font-size: 14px;\"><b>Artifact</b></span>")
            span_row_list = artifacts.findAll("span",{"class":"row"})
            make_row(span_row_list, decks)
            make_row_simple(span_row_list, decks_arena)
        #土地
        lands = player.find('div', class_='sorted-by-land clearfix element')
        if lands:
            decks.append("<span style=\"font-size: 14px;\"><b>Land</b></span>")
            span_row_list = lands.findAll("span",{"class":"row"})
            make_row(span_row_list, decks)
            make_row_simple(span_row_list, decks_arena)
        #サイドボード
        sideboards = player.find('div', class_='sorted-by-sideboard-container clearfix element')
        if sideboards:
            decks.append("<span style=\"font-size: 14px;\"><b>Sideboard</b></span>")
            decks_arena.append("\n\n")
            decks_arena.append("Sideboard")
            span_row_list = sideboards.findAll("span",{"class":"row"})
            make_row(span_row_list, decks)
            make_row_simple(span_row_list, decks_arena)
        decks.append("[/mtg_deck]")
        # MTGACode Botton作成
        today_str = datetime.today().strftime('%Y/%m/')
        mtgacode_url = ("https://teamqno.work/wp-content/uploads/"+ today_str + filename_ + " " + player_name.text + txtfile).replace(' ', '-').replace('(', '').replace(')', '')
        mtgacode_botton = ("[maxbutton id=\"9\" url=\"%s\"]"  % mtgacode_url)
        decks.append(mtgacode_botton)

        csv_data.append('\r\n'.join(decks))

        #アーキタイプカテゴライズ
        if category == categorystan:category_list = [15,34]
        if category == categorystan: results = categorize_decks.check_arc_stan(csv_data)
        if category == categorypio:category_list = [15,36]
        if category == categorypio:results = categorize_decks.check_arc_pion(csv_data)
        post_title = results[0]
        media_id = results[1]
        #タグIDは後程
        title_list = []
        #title_list.append(title)
        #ポスト
        post_article.post_article('draft',post_title,post_title,'\r\n\r\n'.join(csv_data),category_list,title_list,media_id)

        # csvファイル出力用
        final_csv_data.append('')
        final_csv_data.append('')
        final_csv_data.append('qno')
        final_csv_data.append('')
        final_csv_data.append('')
        final_csv_data.append('private')
        final_csv_data.append('')
        final_csv_data.append(post_title)
        final_csv_data.append('\r\n\r\n'.join(csv_data))
        final_csv_data.append(category)
        final_csv_data.append(title)
        final_csv_data.append('')
        final_csv_data.append('')
        csv_write.writerow(csvheader_data)
        csv_write.writerow(final_csv_data)
        # ファイルクローズド
        csv_file.close()
        if os.path.getsize(filename + " " + player_name.text + csvfile) <= 0:
            os.remove(filename + " " + player_name.text + csvfile)
        # MTGArenaファイル出力用
        # ファイル存在チェック
        if os.path.exists(filename + " " + player_name.text + txtfile) and os.path.getsize(filename + " " + player_name.text + txtfile) > 0:
            return
        with open(filename + " " + player_name.text + txtfile, mode='w') as f:
            f.writelines(decks_arena)
        # ファイルクローズド
        f.close()
        if os.path.getsize(filename + " " + player_name.text + txtfile) <= 0:
            os.remove(filename + " " + player_name.text + txtfile)


# デッキリストポストとcsv作成
#スタンダード
title = stdlea + tdyesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath + stdlea + tdyesterday.strftime('-%Y-%m-%d')
filename_ = stdlea + tdyesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title = stdlea + today.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath + stdlea + today.strftime('-%Y-%m-%d')
filename_ = stdlea + today.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title = stdlea + yesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +stdlea + yesterday.strftime('-%Y-%m-%d')
filename_ = stdlea + yesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title = stdlea + dbyesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +stdlea + dbyesterday.strftime('-%Y-%m-%d')
filename_ =stdlea + dbyesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title = stdcha + today.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +stdcha + today.strftime('-%Y-%m-%d')
filename_ = stdcha + today.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title =  stdcha + yesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +stdcha + yesterday.strftime('-%Y-%m-%d')
filename_ = stdcha + yesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title =  stdcha + dbyesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +stdcha + dbyesterday.strftime('-%Y-%m-%d')
filename_ = stdcha + dbyesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title =  stdpre + today.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +stdpre + today.strftime('-%Y-%m-%d')
filename_ = stdpre + today.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title = stdpre + yesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +stdpre + yesterday.strftime('-%Y-%m-%d')
filename_ = stdpre + yesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title =  stdpre + today.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +stdpre + today.strftime('-%Y-%m-%d')
filename_ = stdpre + today.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)

title = stdpre + dbyesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +stdpre + dbyesterday.strftime('-%Y-%m-%d')
filename_ = stdpre + dbyesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorystan)


#パイオニア
title =  piolea + today.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +piolea + today.strftime('-%Y-%m-%d')
filename_ = piolea + today.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorypio)


title =  piolea + yesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +piolea + yesterday.strftime('-%Y-%m-%d')
filename_ = piolea + yesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorypio)


title =  piolea + dbyesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +piolea + dbyesterday.strftime('-%Y-%m-%d')
filename_ = piolea + dbyesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorypio)


title =  piocha + today.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +piocha + today.strftime('-%Y-%m-%d')
filename_ = piocha + today.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorypio)


title = piocha + yesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +piocha + yesterday.strftime('-%Y-%m-%d')
filename_ = piocha + yesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorypio)


title = piocha + dbyesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +piocha + dbyesterday.strftime('-%Y-%m-%d')
filename_ = piocha + dbyesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorypio)


title = piopre + today.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +piopre + today.strftime('-%Y-%m-%d')
filename_ = piopre + today.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorypio)


title =  piopre + yesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +piopre + yesterday.strftime('-%Y-%m-%d')
filename_ = piopre + yesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorypio)


title =  piopre + dbyesterday.strftime('-%Y-%m-%d')
url = mo + title
filename = DeckPath +piopre + dbyesterday.strftime('-%Y-%m-%d')
filename_ = piopre + dbyesterday.strftime('-%Y-%m-%d')
to_csv_mo(url,filename,filename_,title,categorypio)

