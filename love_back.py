#!/usr/bin/python
import praw
import pdb
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("comments_replied_to.txt"):
    comments_replied_to = []

# If we have run the code before, load the list of comments we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("comments_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

# Get the top 10 values from our subreddit
subreddit = reddit.subreddit('ApocalypseWorld')
for submission in subreddit.hot(limit=10): #For every submission
    for comment in submission.comments: #For every comment. Note: Doesn't look into 'Load More' deeper comment trees. Too complicated for such a silly script
        if comment.id not in comments_replied_to:
            if re.search('(?=-*love)(?=.*/u/Apocalypse_bot)', comment.body, re.IGNORECASE): #If bot 'love' and bot's name mentioned in a comment: Reply.
                comment.reply("I love you too /u/" + comment.author.name)
                print("Bot replying to : ", submission.title)
            # Store the current id into our list
                comments_replied_to.append(comment.id)

# Write our updated list back to the file
with open("comments_replied_to.txt", "w") as f:
    for comment_id in comments_replied_to:
        f.write(comment_id + "\n")
