#!/usr/env/bin python

import os

from flask import Flask, g, render_template
from flask.ext.misaka import Misaka
from lib import db, filters 
from themes import themes

from flask.ext.cors import CORS

theme = os.environ.get('THEME', 'new')
blog = Flask(
    __name__,
    static_folder = themes[theme]['static'],
    template_folder = themes[theme]['templates']
)
CORS(blog)
Misaka(blog, tables=True)

blog.config['FREEZER_RELATIVE_URLS'] = True
blog.config['MONGODB_DATABASE_URI'] = 'mongodb://localhost:27017'
blog.config['BASE_DIR'] = os.path.abspath(os.path.dirname(__file__))

blog.jinja_env.filters['human_readable_date'] = filters.human_readable_date
blog.jinja_env.filters['clean_date'] = filters.clean_date
blog.jinja_env.filters['urlencode'] = filters.urlencode
blog.jinja_env.filters['urldecode'] = filters.urldecode
blog.jinja_env.filters['md'] = filters.md

blog.secret_key = 'test'

@blog.errorhandler(404)
def page_not_found(error):
    return render_template('404/index.html'), 404

def connect_db():
    return db.Database(blog.config['MONGODB_DATABASE_URI']) 

@blog.before_request
def before_request():
    g.db = connect_db()

import views 

if not os.environ.get('BUILD'):
    import admin 

print ''' Running on theme {}. '''.format(theme)
