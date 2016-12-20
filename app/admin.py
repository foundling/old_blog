#!/usr/env/bin python

import datetime

from flask import flash, g, redirect, render_template, request, url_for
import slugify

from lib import utils
from app import blog

@blog.route('/admin')
def admin_root():
    ''' populate dashboard view with posts and projects in date-descending order. '''

    posts = reversed( g.db.find_all(collection='post') )
    projects = reversed( g.db.find_all(collection='project') )

    return render_template('admin/dashboard/index.html', posts=posts, projects=projects)

@blog.route('/admin/post/create')
def admin_create_post():
    ''' return view to create a new post '''

    return render_template('admin/post/create.html')

@blog.route('/admin/post/<permalink>/edit')
def admin_edit_post(permalink):
    ''' return view populated with target post values for editing. '''

    document = g.db.find_one({ 'permalink': permalink })
    return render_template('admin/post/edit.html', post=document)

@blog.route('/admin/post/save', methods=['POST'])
def admin_add_post():
    ''' gather form post submission values into a dict, save to post collection in db. ''' 

    is_update = bool(request.form['is_update'])
    form_values = dict((name, value) for name, value in request.form.iteritems())
    complete_post = utils.build_post(form_values, update=is_update)
    if is_update:
        g.db.update_one({'title': complete_post['title']}, complete_post, collection='post')
    else:
        g.db.insert_one(complete_post, collection='post')


    return redirect('/admin')
