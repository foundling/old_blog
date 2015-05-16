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
  posts = [ open(posts_dir + '/' + p).read()\
            for p in os.listdir(posts_dir) 
            if p.endswith('.md')
          ]
  last_five_posts = posts[len(posts) - 5:]
  return posts 

if __name__ == '__main__':
  last_n = last_n_posts(5)
  print len(last_n) 
