'''
Created on 30 Nov 2015

@author: ckaidos
'''
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text
    def on_error(self, status_code):
        print status_code

consumer_key='jdYhlVskWEFOqdSKD9wih3Zsv'
consumer_secret='Qer1bzwSXFVzj5EzOTQetIJ6IHYWcLrfhoqHc5HKq0NJBqEEaX'
access_token_key='18916197-KDEBnuYbOa1oBMdpCKWI43VJcf001Cvay5eL6KviB'
access_token_secret='HB5Jm2Nta5eDTHQYmEhrdC0tMB5YwSSyz5QufUhngy78G'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['#yolo'])
'''track=['#yolo'],''' 
'''locations=[40.968549, 19.385095, 34.585731, 29.779638]'''