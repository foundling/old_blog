#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import sys

def datesort(filename):
  '''
     A key function for the sorted() built-in. Parses the filename's
     date information into a large int for numeric comparison.
  ''' 
  datestring = filename.strip('.md').split('__')[1].replace('_','')
  return int(datestring)

def last_n_posts(n,posts_dir='/data/newblog/static/posts/published'):
  ''' 
     Returns the 5 newest posts by title, author and short_text
  '''

  n_posts = [ posts_dir + '/' + filename for filename 
              in os.listdir(posts_dir) 
              if filename.endswith('.md') ]
  #n_posts.sort(key=datesort)

  posts_content = [ open(post).read()
                   for post in n_posts ]

  post_bundles = []
  for post in posts_content:
    try:
      title = re.findall(r'^(title:.*[a-zA-Z]) *\n',post,re.MULTILINE)[0]
      title = title.split(':')[1].strip()

    except IndexError:
      title = ''

    try:
      author = re.findall(r'^(author:.*[a-zA-Z]) *\n',post,re.MULTILINE)[0] 
      author = author.split(':')[1].strip()

    except IndexError:
      author = ''

    try:
      short_text = re.findall(r'^(short_text:.*[a-zA-Z][.?!]) *\n',
                              post,re.MULTILINE)[0] 
      short_text = short_text.split(':')[1].strip()
    except IndexError:
      short_text = ''

    post_bundles.append([title,author,short_text]) 
 
  return post_bundles[n] 

if __name__ == '__main__':
  for p in last_n_posts(3):
    print p
