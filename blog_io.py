import re
import os
# -*- coding: utf-8 -*-

def datesort(filename):
  '''
     Datesort. A key function for the sorted() built-in. Parses the filename's
     date information into a large int for numeric comparison.
  ''' 
  datestring = filename.strip('.md').split('__')[1]
  datestring = datestring.replace('_','')
  return int(datestring)

def last_n_posts(n,posts_dir='/data/newblog/static/posts/published'):
  ''' returns 5 newest posts and titles '''
  post_content = [ open(posts_dir + '/' + p).read()\
                   for p in os.listdir(posts_dir) 
                     if p.endswith('.md')
                 ]
  titles = []
  for post in post_content:
    try:
      title = re.findall('title: (.*) -->',post)[0]
    except IndexError:
      title = ''
    titles.append(title)
 
  return map(None,titles,post_content)[-5:]

if __name__ == '__main__':
  for i in last_n_posts(5):
    print i[0]
