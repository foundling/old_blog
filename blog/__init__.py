#!/usr/env/bin python

import os

from flask import Flask
from flask.ext.misaka import Misaka
from lib import filters 
from themes import themes

from flask.ext.cors import CORS

theme = os.environ.get('THEME', 'default')

application = Flask(
    __name__,
    static_folder = themes[theme]['static'],
    template_folder = themes[theme]['templates']
)
CORS(application)
Misaka(application)

application.config['FREEZER_RELATIVE_URLS'] = True
application.config['MONGODB_DATABASE_URI'] = 'mongodb://localhost:27017'
application.config['BASE_DIR'] = os.path.abspath(os.path.dirname(__file__))
application.jinja_env.filters['human_readable_date'] = filters.human_readable_date

import views 


print '''
Running on theme {}. To develop on an alternate theme, run: 

    THEME='<THEME_NAME>' python run.py

Available themes: {}

'''.format(theme, ', '.join(themes.keys()))
