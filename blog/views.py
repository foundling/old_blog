#!/usr/env/bin python

from bson import json_util
from json import dumps

import os
import sys

from flask import jsonify, render_template, redirect, request, url_for 
from pymongo import MongoClient

from blog import application
from lib import db, utils

db = db.Database(application.config['MONGODB_DATABASE_URI']) 

## Blog Views 

@application.route('/')
@application.route('/index')
def latest_posts():
    latest_posts = db.find_n_most_recent(5)
    return render_template('index.html',posts=latest_posts)

# all posts
@application.route('/archive')
def all_posts():
    query = request.args.get('query')
    posts = db.find_all()
    return render_template('archive.html', query=query, posts=posts)

# posts by id
@application.route('/posts/<int:post_id>')
def single_blog_post(post_id):
      # so add a layer that splits on - and rejoins / manipulates the text however the db needs it
    post = db.find_one({'post_id': post_id})
    print type(post_id)
    return render_template('posts/single_blog_post.html', post=post)
  

@application.route('/projects/<post_name>')
def projects_by_name(post_name):

    return render_template('single_project.html')

@application.route('/projects')
def projects_all():
    projects = db.find_all({}, collection='projects')
    return render_template('projects.html', projects=projects)

@application.route('/about')
def about_me():
    about_me = db.find_one({'title':'About Me'},collection='static')
    return render_template('about.html', about_me=about_me)

@application.route('/fun/photos/<collection_name>')
def photos(collection_name):
    print collection_name
    collection = {
        'name' : collection_name,
        'photos': os.listdir(os.path.join(application.config['BASE_DIR'],'static/img/static/' + collection_name + '/med'))
    }
    print 'PHOTOS: ', photos
    return render_template('fun.html',collection=collection) 

@application.route('/fun/music')
def music():
    return 'not implemented' 

@application.route('/guides')
def guides():
    return 'not implemented' 

@application.route('/guides/<guide_name>')
def guides_by_name(guide_name):
    return render_template('single_guide.html')

## REST API 

@application.route('/archive/all_posts')
def get():
    result = db.find_all()
    posts = dumps(result, default=json_util.default)
    return jsonify(data=posts)
