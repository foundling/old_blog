#!/usr/env/bin python

from flask import redirect, render_template, request, url_for

from lib import utils, db
from app import blog

db = db.Database( blog.config['MONGODB_DATABASE_URI'] ) 


@blog.route('/admin')
def admin_index():

    posts = reversed( db.find_all(collection='posts') )
    projects = reversed( db.find_all(collection='projects') )

    return render_template('admin/dashboard/index.html', posts=posts, projects=projects)

@blog.route('/admin/edit/posts/<int:post_id>')
def admin_edit_post(post_id):

    post = db.find_one({'post_id': post_id}, collection='posts')
    return render_template('admin/edit/index.html', post=post)


@blog.route('/admin/edit/projects/<int:project_id>')
def admin_edit_project(project_id):

    project = db.find_one({'project_id': project_id}, collection='projects')
    return render_template('admin/edit/index.html', project=project)

@blog.route('/admin/add/posts')
def admin_add_post():
    return render_template('admin/add/index.html')

@blog.route('/admin/<collection_name>/edit/update', methods=['POST'])
def admin_save(collection_name):
    updates = dict((key, value) for key, value in request.form.iteritems())

    db.update(updates, collection=collection_name)
    return redirect('/admin')
