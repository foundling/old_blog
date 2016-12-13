#!/usr/env/bin python

import os

from flask import Flask
from flask.ext.misaka import Misaka
from lib import filters 
from themes import themes

from flask.ext.cors import CORS

theme = os.environ.get('THEME', 'default')

print themes
blog = Flask(
    __name__,
    static_folder = themes[theme]['static'],
    template_folder = themes[theme]['templates']
)
CORS(blog)
Misaka(blog)

blog.config['FREEZER_RELATIVE_URLS'] = True
blog.config['MONGODB_DATABASE_URI'] = 'mongodb://localhost:27017'
blog.config['BASE_DIR'] = os.path.abspath(os.path.dirname(__file__))
blog.jinja_env.filters['human_readable_date'] = filters.human_readable_date
blog.jinja_env.filters['clean_date'] = filters.clean_date

import views 

print '''
Running on theme {}. THEME='<THEME_NAME>' python run.py
'''.format(theme, ', '.join(themes.keys()))
