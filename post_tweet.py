#coding: UTF-8

import twitter

auth = twitter.OAuth(consumer_key="T3FocWPvj7i4F7odzXTgdrT4t",
                    consumer_secret="MXPSm0nxzfrn6XzBWfFZMqBAJay1yVFJXrB12pGrkcg83QMJgF",
                    token="1276917839291506688-Bf37FxFO3DkQxjexNyNjSbr4dKyJBJ",
                    token_secret="a2zeSdXaTI9EGlftKUzJ5woQ7DiFMgtCjvioamt703fb1")

def post_tweet(self, text):
    tw = twitter.Twitter(auth=self.auth)
    # twitterへメッセージを投稿する
    tw.statuses.update(status=text)