#!/usr/env/bin python

import os

from flask import Flask
from flask.ext.misaka import Misaka
from lib import filters 

from flask.ext.cors import CORS

application = Flask(__name__)
CORS(application)

application.config['FREEZER_RELATIVE_URLS'] = True
application.config['MONGODB_DATABASE_URI'] = 'mongodb://localhost:27017'
application.config['BASE_DIR'] = os.path.abspath(os.path.dirname(__file__))
application.jinja_env.filters['human_readable_date'] = filters.human_readable_date
Misaka(application)

import views 
