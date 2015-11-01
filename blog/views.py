#!/usr/env/bin python

import os
import sys

from flask import url_for, render_template, redirect, request
from pymongo import MongoClient

from blog import app
from db_ops import n_most_recent, find_by_id
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
def latest_posts():
  latest_posts = n_most_recent(db,5)
  return render_template('index.html',posts=latest_posts)

# all posts
@app.route('/blog/archive')
def all_posts():
  all_posts = n_most_recent(db,0) # 0 means all
  return render_template('archive.html',posts=all_posts)

# posts by id
@app.route('/posts/<int:post_id>')
def single_blog_post(post_id):
  # so add a layer that splits on - and rejoins / manipulates the text however the db needs it
  post = find_by_id(db, post_id)
  print type(post_id)
  return render_template('single_blog_post.html', post=post)


@app.route('/projects/<post_name>')
def projects_by_name(post_name):

  return render_template('single_project.html')

@app.route('/projects')
def projects_all():
  projects = [
    {'name':'this website'},
    {'name':'node-help'},
    {'name':'list'},
    {'name':'coaster'},
    {'name':'task'},
    {'name':'billing interface'}
  ]
  return render_template('projects.html', projects=projects)

@app.route('/about')
def about_me():

  return render_template('about.html')

@app.route('/fun')
def fun():
  return render_template('fun.html')

@app.route('/guides')
def guides():
  return render_template('guides.html')

@app.route('/guides/<guide_name>')
def guides_by_name(guide_name):
  return render_template('single_guide.html')
