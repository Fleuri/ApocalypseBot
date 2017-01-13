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

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        comments_replied_to = f.read()
        comments_replied_to = comments_replied_to.split("\n")
        comments_replied_to = list(filter(None, comments_replied_to))

# Get the top 5 values from our subreddit
subreddit = reddit.subreddit('apocalypseworld')
for submission in subreddit.hot(limit=10):
    for comment in submission.comments:
        if comment.id not in comments_replied_to:
            print(comment.body)
            if re.search('(?=-*love)(?=.*/u/Apocalypse_bot)', comment.body, re.IGNORECASE):
                comment.reply("I love you too /u/" + comment.author.name)
                print("Bot replying to : ", submission.title)
            # Store the current id into our list
                comments_replied_to.append(comment.id)

# Write our updated list back to the file
with open("comments_replied_to.txt", "w") as f:
    for post_id in comments_replied_to:
        f.write(post_id + "\n")
