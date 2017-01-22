#!/usr/bin/python
import praw
import re
from random import randint


def process_comments():
    reddit = praw.Reddit('bot1')

    for comment in reddit.subreddit('pythonforengineers').stream.comments():
         if re.search('!roll', comment.body, re.IGNORECASE):
             reply= comment.reply(roll())
             print("Replying: " + reply.body)

def roll():

    roll1 = d6()
    roll2 = d6()
    return "Rolled {0} + {1} = {2}".format(roll1, roll2, (roll1+roll2))

def d6():
    return randint(1,6)

if __name__ == '__main__':
    process_comments();