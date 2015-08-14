#!/usr/bin/env python

# 1: establish user input -> mongodb commit pipeline
# 2: establish default/specified  behavior for input
# 3: write any parsing functions needed 

import datetime
import json
import os 
import pprint
import sys

from pymongo import MongoClient 

def usage():
    usage_text = 'usage: publish file1'
    print usage_text

def establish_connection(host='localhost',port='27017'):
    client = MongoClient(''.join([
                                    'mongodb://',
                                    host,
                                    ':',
                                    port,
                                    '/',
                                    ])
                                 )
    db = client.blog
    collection = db.posts
    return client if collection else False

def get_short_text(file_content):
    max_chars  = 80 
    first_sentence = file_content.split('.')[0]
    return first_sentence + '.' if len(first_sentence) <= max_chars else first_sentence + ' ... ' 

def insert_blog_post(title,author,short_text,content,keyworks,date_published):
    pass

def get_user_values(post):
    prompt_questions = {
                            'title':'Title:',
                            'author':'Author:',
                            'keywords':'Keywords:',
                        }
    for category in prompt_questions:
        if category == 'keywords':
            raw_kw_string = raw_input(prompt_questions[category])
            post[category] = [ kw.strip() for kw in raw_kw_string.split(',') ] 
        else:
            post[category] = raw_input(prompt_questions[category])

    return post

def get_automatic_values(post):
    post['date_published'] = datetime.datetime.now() 
    post['content'] = open(sys.argv[1]).read().decode('utf-8')
    post['short_text'] = get_short_text(post['content'])

    return post


def main():
    post = {}
    post = get_user_values(post)
    post = get_automatic_values(post)

    client = establish_connection()
    if client: 
        print 'client successfully established. posts collection works!'
        client.blog.posts.insert_one(post)
        client.close()
    else:
        print 'client connection was unsuccessful'

if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        sys.exit()

    else:
        main()

