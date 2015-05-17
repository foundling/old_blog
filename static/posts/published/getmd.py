#!/usr/bin/env python
import re
import sys

def get_metadata(content):
  try:
    title = re.findall(r'^title:.*[a-zA-Z]',content,re.MULTILINE)[0]
  except IndexError:
    title = ''
  try:
    author = re.findall(r'^author:.*[a-zA-Z]',content,re.MULTILINE)[0]
  except IndexError:
    author = ''
  return title, author

for f in sys.argv[1:]:
  content = open(f).read()
  print get_metadata(content)
