from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo


wp = Client('https://teamqno.work/xmlrpc.php', 'qno', 'Team-9no')

result = wp.call(GetPosts())
 
#全記事のタイトルを出力
for post in result:
    print(post)

#全記事のIDを出力、Pythonの原則通りインスタンスのアトリビュート（プロパティ）にアクセス
for post in result:
    print(post.id)
 
#辞書型により抽出条件の設定
result = wp.call(GetPosts({'post_status':'private'})) 
 
for post in result:
    print(post)