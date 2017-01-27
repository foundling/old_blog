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

    query = {
        'content_type': {
            '$in': ['article', 'news', 'quick_tip']
        }
    }

    latest_posts = g.db.find_n_most_recent(n=5, query=query)
    return render_template('index.html', posts=latest_posts)
 
@blog.route('/blog/')
def blog_main():

    query = {
        'content_type': {
            '$in': ['article', 'news', 'quick_tip']
        }
    }

    latest_posts = g.db.find_n_most_recent(n=5, query=query)
    return render_template('index.html', posts=latest_posts)
 
@blog.route('/blog/recent')
def recent_articles():
    posts = g.db.find_n_most_recent(n=5, query={'content_type': 'article'})
    return render_template('index.html', posts=posts)

@blog.route('/blog/<permalink>/')
def single_post(permalink):
    post = g.db.find_one({'permalink': permalink})
    return render_template('post/single_post.html', post=post)

@blog.route('/archive/')
def archive():
    return render_template('archive.html')

#@blog.route('/projects/')
# def projects():
#     projects = g.db.find_all({}, collection='projects')
#     return render_template('projects.html', projects=projects)

@blog.route('/news/')
def news():
    posts = g.db.find_all(query={'content_type': 'news'})
    return render_template('news.html', posts=posts)

@blog.route('/quick_tips/')
def quick_tips():
    posts = g.db.find_all(query={'content_type': 'quick_tip'})
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
