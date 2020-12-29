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

three_weeks_ago = datetime.today() + timedelta(weeks=-3)
two_weeks_ago = datetime.today() + timedelta(weeks=-2)
one_weeks_ago = datetime.today() + timedelta(weeks=-1)
today_str = datetime.today().strftime('%Y/%m/%d')

def get_graph_stan(weeks_ago):
    metadeck = []
    for i in range(50):
        #URL Pageループ
        url ="https://teamqno.work/category/decks/standard-metagame/page/{}".format(i+1)
        #print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        decks = soup.findAll('div', class_='entry-card-content card-content e-card-content')
        #デッキループ
        for deck in decks:
            deck_name = deck.find('h2', class_='entry-card-title card-title e-card-title')
            deck_post_date = deck.find("span",{"class":"post-date"})
            # 日付比較
            # 基準日の1週間前を算出
            date_str=deck_post_date.get_text()
            #print(date_str)
            tdatetime = datetime.strptime(date_str, ' %Y.%m.%d')

            #print(one_weeks_ago<=tdatetime)
            if weeks_ago<=tdatetime:
                metadeck.append(deck_name.get_text())


    #グラフ出力
    mycounter = Counter(metadeck)
    index, data = zip(*mycounter.most_common())
    #print(list(index))
    #print(list(data))
    ns = map(lambda s: int(s), list(data))
    tindex = list(index)
    tdata = list(ns)
    tindex.reverse()
    tdata.reverse()
    #print(tindex)
    #print(tdata)
    xlabel = "Standard Metagame " + weeks_ago.strftime('%Y/%m/%d')  + " - "  + today_str + " by Team Qno Research"
    #print(xlabel)
    output_graph.make_graph(tindex,tdata,xlabel)
    return

def get_graph_hist(weeks_ago):
    metadeck = []
    for i in range(50):
        #URL Pageループ
        url ="https://teamqno.work/category/decks/historic-metagame//page/{}".format(i+1)
        #print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        decks = soup.findAll('div', class_='entry-card-content card-content e-card-content')
        #デッキループ
        for deck in decks:
            deck_name = deck.find('h2', class_='entry-card-title card-title e-card-title')
            deck_post_date = deck.find("span",{"class":"post-date"})
            # 日付比較
            date_str=deck_post_date.get_text()
            #print(date_str)
            tdatetime = datetime.strptime(date_str, ' %Y.%m.%d')

            #print(one_weeks_ago<=tdatetime)
            if weeks_ago<=tdatetime:
                metadeck.append(deck_name.get_text())


    #グラフ出力
    mycounter = Counter(metadeck)
    index, data = zip(*mycounter.most_common())
    #print(list(index))
    #print(list(data))
    ns = map(lambda s: int(s), list(data))
    tindex = list(index)
    tdata = list(ns)
    tindex.reverse()
    tdata.reverse()
    #print(tindex)
    #print(tdata)
    xlabel = "Historic Metagame " + weeks_ago.strftime('%Y/%m/%d') + " - "  + today_str + " by Team Qno Research"
    #print(xlabel)
    output_graph.make_graph(tindex,tdata,xlabel)
    return

def get_graph_pion(weeks_ago):
    metadeck = []
    for i in range(50):
        #URL Pageループ
        url ="https://teamqno.work/category/decks/pioneer-metagame//page/{}".format(i+1)
        #print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        decks = soup.findAll('div', class_='entry-card-content card-content e-card-content')
        #デッキループ
        for deck in decks:
            deck_name = deck.find('h2', class_='entry-card-title card-title e-card-title')
            deck_post_date = deck.find("span",{"class":"post-date"})
            # 日付比較
            date_str=deck_post_date.get_text()
            #print(date_str)
            tdatetime = datetime.strptime(date_str, ' %Y.%m.%d')

            #print(one_weeks_ago<=tdatetime)
            if weeks_ago<=tdatetime:
                metadeck.append(deck_name.get_text())


    #グラフ出力
    mycounter = Counter(metadeck)
    index, data = zip(*mycounter.most_common())
    #print(list(index))
    #print(list(data))
    ns = map(lambda s: int(s), list(data))
    tindex = list(index)
    tdata = list(ns)
    tindex.reverse()
    tdata.reverse()
    #print(tindex)
    #print(tdata)
    xlabel = "Pioneer Metagame " + weeks_ago.strftime('%Y/%m/%d') + " - "  + today_str + " by Team Qno Research"
    #print(xlabel)
    output_graph.make_graph(tindex,tdata,xlabel)
    return


# 実行
#get_graph_stan(one_weeks_ago)
get_graph_hist(one_weeks_ago)
#get_graph_pion(one_weeks_ago)
# get_graph_pion(two_weeks_ago)
# get_graph_pion(three_weeks_ago)
