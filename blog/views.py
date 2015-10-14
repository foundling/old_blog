#!/usr/env/bin python

import os
import sys

from flask import url_for, render_template, redirect, request
from pymongo import MongoClient

from blog import app
from db_ops import n_most_recent
from config import config
from utilities import print_config_values, connect


''' Initialization Stuff '''

print_config_values()
client = connect()
if client:
  db = client.blog
else:
  print 'your mongo server is not running'
  sys.exit(1)



@app.route('/')
@app.route('/index.html')
def index():
  # should show last five posts
  # at end, a link to archive
    latest_posts = n_most_recent(db,5)
    print latest_posts
    return render_template('index.html',latest_posts=latest_posts)

@app.route('/resume.html')
def resume():
  return render_template('resume.html')
#
#@app.route('/archive')
#def archive():
#  # page has categories, sort filter, search bar, gets results via ajax 
#  # shows posts by date only, by keyword relevance, by keyword and date
#  titles_and_content = last_n_posts(5)
#  return render_template('archive.html',last_five_posts=titles_and_content)
#
## /index acts as /tutorials
#@app.route('/tutorials/<path:name>')
#def tutorial_single(name):
#  # fetch tutorial from db
#  # render tutorial template
#  # name should have n dashes: things-i-learned-this-year,
#  # so add a layer that splits on - and rejoins / manipulates the text however the db needs it
#  return name
#
#@app.route('/writing')
#def writing_stubs():
#  return render_template('writing.html')
#
#@app.route('/writing/<path:name>')
#def writing_single():
#  return render_template('writing.html')
#
#@app.route('/about-me')
#def about_me():
#  # a page that doesn't inherit from base.  Content at top about me, my goals, interests, skills
#  # then a list of projects w/ screenshots and links to them
#  return render_template('about-me.html')
#
#@app.route('/fun')
#def fun():
#  # another page that doesn't inherit from base. similar to about-me, a free-flowing, lazy-loading stream
#  # of stuff I'm interested in and do: photos, drawings, music  etc
#  return render_template('fun.html')
#
#@app.route('/guides/js')
#def guides_js():
#  return render_template('js_guide.html')
#
#@app.route('/guides/python')
#def guides_python():
#  return render_template('python_guide.html')
