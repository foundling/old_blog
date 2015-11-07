#!/usr/env/bin python

import os

from flask import Flask
from flask.ext.misaka import Misaka
from lib import filters 

from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

app.config['FREEZER_RELATIVE_URLS'] = True
app.config['MONGODB_DATABASE_URI'] = 'mongodb://localhost:27017'
app.jinja_env.filters['human_readable_date'] = filters.human_readable_date
Misaka(app)

import views 
