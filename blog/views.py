#!/usr/env/bin python

import os
import sys

from flask import jsonify, render_template, redirect, request, url_for 
from pymongo import MongoClient

from blog import app
from lib import db, utils

db = db.Database(app.config['MONGODB_DATABASE_URI']) 

## Blog Views 

@app.route('/')
@app.route('/index/')
def latest_posts():
  latest_posts = db.find_n_most_recent(5)
  return render_template('index.html',posts=latest_posts)

# all posts
@app.route('/blog/archive')
def all_posts():
  return render_template('archive.html')

# posts by id
@app.route('/posts/<int:post_id>')
def single_blog_post(post_id):
  # so add a layer that splits on - and rejoins / manipulates the text however the db needs it
  post = db.find_one({'post_id': post_id})
  print type(post_id)
  return render_template('single_blog_post.html', post=post)


@app.route('/projects/<post_name>')
def projects_by_name(post_name):

  return render_template('single_project.html')

@app.route('/projects')
def projects_all():
  projects = db.find_all({}, collection='projects')
  return render_template('projects.html', projects=projects)

@app.route('/about')
def about_me():
  about_me = db.find_one({'title':'About Me'},collection='static')
  return render_template('about.html', about_me=about_me)

@app.route('/fun')
def fun():
  return 'not implemented' 

@app.route('/fun/music')
def music():
  return 'not implemented' 

@app.route('/guides')
def guides():
  return 'not implemented' 

@app.route('/guides/<guide_name>')
def guides_by_name(guide_name):
  return render_template('single_guide.html')

## REST API 

@app.route('/api/<string:guide>/<int:chapter>')
def get(guide,chapter,collection='guides'):
  db.find_one()
  data = {'msg':'h1'}
  return jsonify(**data)
