#!/usr/env/bin python

import os

from flask import Flask
from flask.ext.misaka import Misaka

app = Flask(__name__)
Misaka(app)

from blog import views 


