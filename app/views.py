#!/usr/env/bin python

from bson.objectid import ObjectId
import os
import sys

from flask import g, render_template, redirect, request, url_for 
from pymongo import MongoClient

from app import blog
from lib import utils
from themes import themes

@blog.route('/')
def index():
    ## consider adding news sction into this as well, reducing recent posts to 2
    ## blog would then be the full list
    latest_posts = g.db.find_n_most_recent(1)
    return render_template('index.html', posts=reversed(latest_posts))

@blog.route('/blog/')
def blog_main():
    latest_posts = g.db.find_n_most_recent(5)
    return render_template('index.html', posts=reversed(latest_posts))
 
@blog.route('/blog/<permalink>/')
def single_post(permalink):
    post = g.db.find_one({'permalink': permalink})
    return render_template('post/single_blog_post.html', post=post)

@blog.route('/archive/')
def archive():
    query = request.args.get('query')
    posts = reversed(g.db.find_all())
    return render_template('archive.html', query=query, posts=posts)

@blog.route('/projects/')
def projects():
    projects = g.db.find_all({}, collection='projects')
    return render_template('projects.html', projects=projects)

#@blog.route('/about')
#def about_me():
#    about_me = g.db.find_one({'title':'About Me'},collection='static')
#    return render_template('about.html', about_me=about_me)

#@blog.route('/fun/photos/<collection_name>/')
#def photos(collection_name):
#    collection = {
#        'name' : collection_name,
#        'photos': os.listdir(
#            os.path.join(
#                blog.config['BASE_DIR'],
#                'static/img/static',
#                collection_name, 'med'
#            )
#        )
#    }
#    return render_template('fun.html',collection=collection) 
