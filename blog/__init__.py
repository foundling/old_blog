#!/usr/env/bin python

import os

from flask import Flask
from flask.ext.misaka import Misaka
from filters import human_readable_date

app = Flask(__name__)
app.jinja_env.filters['human_readable_date'] = human_readable_date
Misaka(app)


from blog import views 

print __path__
