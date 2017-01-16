#!/usr/bin/python
import praw
import sys

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('ApocalypseWorld')
submission = None
if len(sys.argv) == 2:
    submission = subreddit.submit(sys.argv[1], " ")
elif len(sys.argv) == 3:
    submission = subreddit.submit(sys.argv[1], sys.argv[2])

else:
    print("You must provide arguments (Title, <selftext>)")

submission.mod.sticky()
