#!/usr/bin/env python

import sys
import os

import pymongo

class Database(object):

  def __init__(self, uri, db_name='blog'):

    self.db = self.connect(uri)[db_name]

  def connect(self,uri):

      ''' returns client or exits '''

      server_running = os.system('pgrep mongod > /dev/null') == 0
      if not server_running:
          print 'The mongod server is not running. Try starting it and run the script again.'
          sys.exit(1)

      try:
          client = pymongo.MongoClient(uri, connectTimeoutMS=1000)

      except pymongo.errors.ConnectionFailure:
          print 'could not connect to the database'
          sys.exit(1)

      return client

  def close_connection(self):
      self.db.close_connection()

  def find_one(self, query, collection='post'):
    return self.db[collection].find_one(query)

  def count(self, collection='post'):
    return self.db[collection].count();

  def find_all(self, query={}, collection='post'):
    result_set = self.db[collection].find(query).sort('date', pymongo.ASCENDING)
    return [result for result in result_set]

  def find_n_most_recent(self, n, collection='post'):
    result_set = self.db[collection].find().sort('date', pymongo.ASCENDING)
    return [result for result in result_set]

  def insert_one(self, document, collection='post'):
    print document, collection
    self.db[collection].insert_one(document);

  def update_one(self, query, update, collection='post'):
    ''' 
      note, this uses $set to update one or more fields without replacing entire doc 
      user passes in objects
    '''
    print query
    print update

    # RESUME HERE
    result = self.db[collection].update_one(query, {'$set': update})
    return result.matched_count
