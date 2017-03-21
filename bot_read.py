#!/usr/bin/python
import praw
import re
from random import randint


def process_comments():
    reddit = praw.Reddit('bot1')

    for comment in reddit.subreddit('pythonforengineers').stream.comments():
         if re.search('!roll', comment.body, re.IGNORECASE): #If rolling comment found
             number_of_dice=None
             type=None
             diespec = re.search(r'(?<!\d)\d{1,3}(?!\d)d(?<!\d)\d{1,3}(?!\d)', comment.body) #check if accommodates the form digit-d-digit. Max 3 numbers
             if diespec:
                specs = diespec.group(0).split('d') #Split numbers
                number_of_dice=int(specs[0])
                type=int(specs[1])
             #reply= comment.reply(roll())
             reply = roll(number_of_dice=number_of_dice,type=type) if number_of_dice is not None and type is not None else roll()
             print("Replying: " + reply)

def roll(number_of_dice=2, type=6, stat=0):
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