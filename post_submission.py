#!/usr/bin/python
import praw
import sys

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit('ApocalypseWorld')
submission = None
# If only post name given.
if len(sys.argv) == 2:
    submission = subreddit.submit(sys.argv[1], " ")
# If selftext or url given.
elif len(sys.argv) == 3:
    submission = subreddit.submit(sys.argv[1], sys.argv[2])

else:
    print("You must provide arguments (Title, <selftext/url>)")
# Sticky the post, will return in an error if no moderator rights. The post will be posted nevertheless, just not stickied.
submission.mod.sticky(state=True, bottom=False)
