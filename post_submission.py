import praw
import sys

if len(sys.argv) > 1 and len(sys.argv) < 4:
    reddit = praw.Reddit('bot1')
    subreddit = reddit.subreddit('pythonforengineers')
    submission = subreddit.submit(sys.argv[1],
                     sys.argv[2])
    submission.mod.sticky()
else:
    print("You must provide arguments (Title, <selftext>)")

