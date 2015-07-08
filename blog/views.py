import os
from flask import url_for, render_template, redirect, request

from blog import app
from blog_io import datesort, last_n_posts

POSTS_DIR = 'blog/static/posts/published'

@app.route('/')
def index():
  return redirect(url_for('latest'))

@app.route('/latest')
def latest():
  published_posts = [f for f in os.listdir(POSTS_DIR) if f.endswith('.md')]
  latest_post_filename = sorted(published_posts,key=datesort)[-1]
  latest_post_content = open('/'.join([POSTS_DIR,latest_post_filename])).read()
  latest_post_content
  return render_template('index.html',latest_post=latest_post_content)

@app.route('/archive')
def archive():
  titles_and_content = last_n_posts(5)
  return render_template('archive.html',last_five_posts=titles_and_content)

@app.route('/tutorials')
def tutorials():
  return render_template('archive.html',results=tutorial_results)


