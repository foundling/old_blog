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
    latest_posts = g.db.find_n_most_recent(1)
    return render_template('index.html', posts=latest_posts)

@blog.route('/blog/')
def blog_main():
    latest_posts = g.db.find_n_most_recent(5)
    return render_template('index.html', posts=latest_posts)
 
@blog.route('/blog/<permalink>/')
def single_post(permalink):
    post = g.db.find_one({'permalink': permalink})
    return render_template('post/single_post.html', post=post)

@blog.route('/archive/')
def archive():
    return render_template('archive.html')

#@blog.route('/projects/')
#def projects():
#    projects = g.db.find_all({}, collection='projects')
#    return render_template('projects.html', projects=projects)

@blog.route('/news/')
def news():
    posts = g.db.find_all(query={'is_news': 'on'})
    return render_template('news.html', posts=posts)

@blog.route('/about/')
def about():
    return render_template('about.html')

@blog.route('/search/<search_query>/')
def search(search_query):

    db_query = {
        '$or': [
            {'content': {'$regex': search_query}}, 
            {'title': {'$regex': search_query}},
            {'tags': {'$regex': search_query}}
        ]
    }
    matched = g.db.find_all(query=db_query)
    return render_template('search.html', posts=matched); 

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
