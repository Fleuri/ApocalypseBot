#!/usr/bin/python
import praw
import re
from random import randint


def process_comments():
    reddit = praw.Reddit('bot1')

    for comment in reddit.subreddit('pythonforengineers').stream.comments():
         if re.search('!roll', comment.body, re.IGNORECASE):
             diespec = re.search(r'\dd\d', comment.body)
             if diespec:
                print(diespec.group(0))
                specs = diespec.group(0).split('d')
                print(specs[0])
                print(specs[1])
             #reply= comment.reply(roll())
             reply = roll()
             print("Replying: " + reply)

def roll(number_of_dice=3, type=7, stat=0):
    rolls = []
    total = 0
    i = 0
    while i  < number_of_dice:
        dieroll = die(type)
        rolls.append(dieroll)
        total = total + dieroll
        i=i+1

    rolled = ''
    i = 0
    print(rolls)
    while i <number_of_dice-1:
        print(i)
        rolled = rolled + str(rolls[i]) + " + "
        i = i+1
    rolled = rolled + str(rolls[len(rolls)-1])
    result_string = "Rolled: " + rolled +  " = " + str(total)

    return result_string

def die(type):
    return randint(1,type)

if __name__ == '__main__':
    process_comments();