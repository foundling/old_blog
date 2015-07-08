import os
from flask import url_for, render_template, redirect, request

from blog import app
from blog_io import datesort, last_n_posts

POSTS_DIR = 'blog/static/posts/published'

@app.route('/')
@app.route('/index')
def index():
  # should show last five posts
  # at end, a link to archive
  published_posts = [f for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
  latest_post_filename = sorted(published_posts,key=datesort)[-1]
  latest_post_content = open('/'.join([POSTS_DIR,latest_post_filename])).read()
  latest_post_content
  return render_template('index.html',latest_post=latest_post_content)

@app.route('/archive')
def archive():
  # page has categories, sort filter, search bar, gets results via ajax 
  # shows posts by date only, by keyword relevance, by keyword and date
  titles_and_content = last_n_posts(5)
  return render_template('archive.html',last_five_posts=titles_and_content)

@app.route('/tutorials')
def tutorial_stubs():
  # main page for tutorial stubs
  titles_and_content = last_n_posts(5)
  return render_template('tutorials.html',last_five_posts=titles_and_content)

@app.route('/tutorials/<path:name>')
def tutorial_single(name):
  # fetch tutorial from db
  # render tutorial template
  return name

@app.route('/writing')
def writing_stubs():
  return render_template('writing.html')

@app.route('/writing/<path:name>')
def writing_single():
  return render_template('writing.html')

@app.route('/about-me')
def about_me():
  # a page that doesn't inherit from base.  Content at top about me, my goals, interests, skills
  # then a list of projects w/ screenshots and links to them
  return render_template('about-me.html')

@app.route('/fun')
def fun():
  # another page that doesn't inherit from base. similar to about-me, a free-flowing, lazy-loading stream
  # of stuff I'm interested in and do: photos, drawings, music  etc
  return render_template('fun.html')
