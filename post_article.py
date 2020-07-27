# coding=utf-8
import json
import os
import requests
from urllib.parse import urljoin
from datetime import datetime

# WordPressのデータ
WP_URL = 'https://teamqno.work/'  # 例: 'https://virtual-surfer.com/'
WP_USERNAME = 'qno'
WP_PASSWORD = '3gBL 0aGm cKDt sHnB GC3v xPMO'

def post_article(status, slug, title, content, category_ids, tag_ids, media_id):
   """
   記事を投稿して成功した場合はTrue、失敗した場合はFalseを返します。
   :param status: 記事の状態（公開:publish, 下書き:draft）
   :param slug: 記事識別子。URLの一部になる（ex. slug=aaa-bbb/ccc -> https://wordpress-example.com/aaa-bbb/ccc）
   :param title: 記事のタイトル
   :param content: 記事の本文
   :param category_ids: 記事に付与するカテゴリIDのリスト
   :param tag_ids: 記事に付与するタグIDのリスト
   :param media_id: 見出し画像のID
   :return: レスポンス
   """
   # credential and attributes
   user_ = WP_USERNAME
   pass_ = WP_PASSWORD
   # build request body
   payload = {"status": status,
              "slug": slug,
              "title": title,
              "content": content,
              "date": datetime.now().isoformat(),
              "categories": category_ids,
              "tags": tag_ids}
   if media_id is not None:
       payload['featured_media'] = media_id
   # send POST request
   res = requests.post(urljoin(WP_URL, "wp-json/wp/v2/posts"),
                       data=json.dumps(payload),
                       headers={'Content-type': "application/json"},
                       auth=(user_, pass_))
   print('----------\n件名:「{}」の投稿リクエスト結果:{} res.status: {}'.format(title,"", repr(res.status_code)))
   return res

def post_tag(tag):
    user_ = WP_USERNAME
    pass_ = WP_PASSWORD
    res = requests.post(urljoin(WP_URL,'wp-json/wp/v2/tags'),
                    data=json.dumps({"name":tag, "slug":tag, "description": tag}),
                    headers={'Content-type': "application/json"},
                    auth=(user_, pass_))
    print(res)
    return 

def post_txt(file_path):
    user_ = WP_USERNAME
    pass_ = WP_PASSWORD
    # check local file path
    file_name = os.path.basename(file_path)
    headers_ = {
        "Content-Disposition": 'attachment; filename="{}"'.format(file_name),
        "Content-Type": "application/octet-stream"}
    # read local picture file
    with open(file_path, 'rb') as f:
        txt_data = f.read()
    # send POST request
    res = requests.post(urljoin(WP_URL,"wp-json/wp/v2/media/"),
                        data=txt_data,
                        headers=headers_,
                        auth=(user_, pass_))
    print(repr(res))

#post_txt(r"E:\TeamQno\Decks\Pioneer-Preliminary-2020-07-14 azax (3-2).txt")

def get_tags():
    # credential and attributes
    user_ = WP_USERNAME
    pass_ = WP_PASSWORD
    ids = []
    params = {"page": 1,"per_page": 100,"order": "desc","orderby": "id"}
    res = requests.get(urljoin(WP_URL, "wp-json/wp/v2/tags"),
                        params=params,
                        headers={'Content-type': "application/json"},
                        auth=(user_, pass_))
    #valuesで値をとってくる
    for v in res.json():
        ids.append(v["id"])
    return ids[0]