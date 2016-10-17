#!/usr/env/bin python

import os
import sys

from bson import json_util
from json import dumps

from flask import jsonify, render_template, redirect, request, url_for 
from pymongo import MongoClient

from blog import application
from lib import db, utils

db = db.Database(application.config['MONGODB_DATABASE_URI']) 

@application.route('/')
@application.route('/index.html')
def latest_posts():
    latest_posts = db.find_n_most_recent(5)
    return render_template('index.html',posts=reversed(latest_posts))
 
@application.route('/posts/<int:post_id>/')
def single_blog_post(post_id):
    post = db.find_one({'post_id': post_id})
    return render_template('posts/single_blog_post.html', post=post)

@application.route('/archive/')
def all_posts():
    query = request.args.get('query')
    posts = reversed(db.find_all())
    return render_template('archive.html', query=query, posts=posts)

@application.route('/projects/')
def projects_all():
    projects = db.find_all({}, collection='projects')
    return render_template('projects.html', projects=projects)

@application.route('/about/')
def about_me():
    about_me = db.find_one({'title':'About Me'},collection='static')
    return render_template('about.html', about_me=about_me)

@application.route('/fun/photos/<collection_name>/')
def photos(collection_name):
    collection = {
        'name' : collection_name,
        'photos': os.listdir(os.path.join(application.config['BASE_DIR'],'static/img/static/' + collection_name + '/med'))
    }
    return render_template('fun.html',collection=collection) 
