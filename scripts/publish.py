#!/usr/bin/env python
''' 

    This script takes a file path as an argument and does the following:
        - creates a post object
        - takes user input regarding the post name, author and keywords
        - adds these to the object
        - reads the file content and calculates an excerpt
        - adds these to the object
        - connects to a mongodb 'blog' database 'post' collection
        - inserts the post object into the post collection
        - asserts that the same thing that was inserted is retrievable

'''

import datetime
import json
import os 
import pprint
import sys

from pymongo import MongoClient 

def usage():
    usage_text = 'usage: publish file1'
    print usage_text

def get_short_text(file_content):
    max_chars  = 80 
    first_sentence = file_content.split('.')[0]
    return first_sentence + '.' if len(first_sentence) <= max_chars else first_sentence + ' ... ' 


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

def connect(host='localhost',port='27017'):
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



def main():
    post = {}
    post = get_user_values(post)
    post = get_automatic_values(post)

    client = connect()

    if not client: 
        print 'client connection was unsuccessful'
        sys.exit()
    
    print 'client successfully established. posts collection works!'
    client.blog.posts.insert_one(post)
    # here, you assert that the post is what you inserted
    client.close()

if __name__ == '__main__':

    if len(sys.argv) < 2:
        usage()
        sys.exit()

    else:
        main()
