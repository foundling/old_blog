#!/usr/env/bin python

import datetime

from bson.objectid import ObjectId
from flask import flash, g, redirect, render_template, request, url_for
import slugify

from lib import utils, md_to_menu
from app import blog

@blog.route('/admin/')
def admin_root():
    ''' Populate dashboard view with posts and projects in date-descending order. '''

    posts =  g.db.find_all(query={'content_type':{'$in': ['article','news','project']}})
    projects = g.db.find_all(query={'content_type':'project'})

    return render_template('admin/dashboard/index.html', posts=posts, projects=projects)

@blog.route('/admin/post/create/')
def admin_create_post():
    ''' Return view to create a new post '''

    return render_template('admin/post/create.html')


@blog.route('/admin/project/create')
def admin_create_project():
    return 'project'

@blog.route('/admin/post/new/save', methods=['POST'])
def admin_save_new_post():
    ''' Gather form post submission values into a dict, save to post collection in db. ''' 
    
    fields = ['title', 'short_text', 'content', 'tags', 'content_type']
    document = dict((field, request.form.get(field)) for field in fields)
    complete_post = utils.add_metadata(document)
    g.db.insert_one(complete_post)

    return redirect('/admin')

@blog.route('/admin/post/<id>/edit')
def admin_edit_post(id):
    ''' Return view populated with target post values for editing. '''

    document = g.db.find_one({ '_id': ObjectId(id) })
    return render_template('admin/post/edit.html', post=document)

@blog.route('/admin/post/<id>/save', methods=['POST'])
def admin_save_existing_post(id):
    ''' Save an existing post. '''

    query = { '_id': ObjectId(id) }
    fields = ['title', 'short_text', 'content', 'tags', 'content_type']
    document = dict((field, request.form.get(field)) for field in fields)
    update = utils.add_metadata(document, update=True) 

    g.db.update_one(update, query=query)
    return redirect('/admin')

@blog.route('/admin/post/<id>/delete', methods=['POST'])
def admin_delete_post(id):
    ''' Delete post by id. '''

    query = { '_id': ObjectId(id) }
    g.db.remove(query)

    return redirect('/admin')
