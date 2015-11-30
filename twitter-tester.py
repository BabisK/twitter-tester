'''
Created on 30 Nov 2015

@author: ckaidos
'''
import twitter

api = twitter.Api(consumer_key='jdYhlVskWEFOqdSKD9wih3Zsv', consumer_secret='Qer1bzwSXFVzj5EzOTQetIJ6IHYWcLrfhoqHc5HKq0NJBqEEaX', access_token_key='18916197-KDEBnuYbOa1oBMdpCKWI43VJcf001Cvay5eL6KviB', access_token_secret='HB5Jm2Nta5eDTHQYmEhrdC0tMB5YwSSyz5QufUhngy78G')
print api.VerifyCredentials()

statuses = api.GetUserTimeline(screen_name='brickoffthewall')
print [s.text for s in statuses]

users = api.GetFriends()
print [u.name for u in users]

yolos = api.GetSearch(term='#yolo', count=10)
print [yolo.text for yolo in yolos]

for yolo in api.GetStreamFilter(track=['#yolo', '#YOLO'], stall_warnings=True):
    print yolo['text']