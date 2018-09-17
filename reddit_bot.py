import praw
import sys
import random

reddit = praw.Reddit(client_id='d**********',
                     client_secret='w*************',
                     user_agent='Memes!',
                     username='h*****',
                     password='c*******')

subreddit = reddit.subreddit('funny+memes+meme+WTF+Showerthoughts+')
random.seed(69)
for submission in subreddit.stream.submissions():
    x = random.randint(1,10000000)
    f1 = open("memes_bot.data", "ab")
    f1.write("0|" + submission.title.encode('utf-8') + "|"+ submission.subreddit_name_prefixed.encode('utf-8') + "|"+ str(x) +"\n")
    f1.close()
