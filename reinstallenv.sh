#!/bin/bash

sudo rm -rf ./env
virtualenv -p /usr/bin/python3.5 ./env
./env/bin/pip install praw
cp ~/praw.ini ./env/lib/python3.5/site-packages/praw/praw.ini

