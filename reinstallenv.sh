#!/bin/bash

sudo rm -rf ./env
virtualenv -p /usr/local/bin/python3.5 ./env
./env/bin/pip install praw
cat ~/praw.ini >> ./env/lib/python3.5/site-packages/praw/praw.ini

