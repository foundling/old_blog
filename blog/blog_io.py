#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import os
import re
import sys

def datesort(filename):
  '''
     A key function for the sorted() built-in. Parses the filename's
     date information into a large int for numeric comparison.
  ''' 
  datestring = filename.strip('.md').split('__')[1].replace('_','')
  return int(datestring)

def fname_to_datetime(fname):
  fname = fname.replace('.md','')
  fname = fname.split('__')[1]
  time_vals = map(int,fname.split('_'))
  return datetime(*time_vals)
  # to improve: 
  # http://stackoverflow.com/questions/13855111/how-can-i-convert-24-hour-time-to-12-hour-time
  # d = datetime.strptime("10:30", "%H:%M")
  # d.strftime("%I:%M %p")

def last_n_posts(n,posts_dir='/data/web/blog/blog/static/posts/published'):
  ''' 
     Returns the 5 newest posts by title, author and short_text
  '''

  n_posts = sorted([ posts_dir + '/' + filename 
              for filename 
              in os.listdir(posts_dir) 
              if filename.endswith('.md') ], key=datesort, reverse=True)

  posts_content = [ open(post).read()
                   for post in n_posts ]

  posts_data = []
  for content in posts_content:
    try:
      title = re.findall(r'^(title:.*[a-zA-Z]) *\n',content,re.MULTILINE)[0]
      title = title.split(':')[1].strip()

    except IndexError:
      title = ''

    try:
      author = re.findall(r'^(author:.*[a-zA-Z]) *\n',content,re.MULTILINE)[0] 
      author = author.split(':')[1].strip()

    except IndexError:
      author = ''

    try:
      short_text = re.findall(r'^(short_text:.*[a-zA-Z][.?!]) *\n',
                              content,re.MULTILINE)[0] 
      short_text = short_text.split(':')[1].strip()
    except IndexError:
      short_text = ''

    posts_data.append(dict(content=content,
                           title=title,
                           author=author,
                           short_text=short_text)
                      ) 
 
  return posts_data 

if __name__ == '__main__':
  print fname_to_datetime('getting_started_with_sed__2015_05_10_20_01_31.md') 
