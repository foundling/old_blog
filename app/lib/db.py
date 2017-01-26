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
          print('The mongod server is not running. Try starting it and run the script again.')
          sys.exit(1)

      try:
          client = pymongo.MongoClient(uri, connectTimeoutMS=1000)

      except pymongo.errors.ConnectionFailure:
          print('could not connect to the database')
          sys.exit(1)

      return client

  def close_connection(self):

    self.db.close_connection()

  def find_one(self, query={}, collection='post'):

    return self.db[collection].find_one(query)

  def count(self, query={}, collection='post'):

    return self.db[collection].find(query).count();

  def find_all(self, query={}, collection='post'):

    result_set = self.db[collection].find(query).sort('date', pymongo.DESCENDING)
    return [result for result in result_set]

  def find_n_most_recent(self, n=5, query={}, collection='post'):

    result_set = self.db[collection].find(query).sort('date', pymongo.DESCENDING)
    return [result for result in result_set]

  def insert_one(self, document, collection='post'):

    self.db[collection].insert_one(document);

  def remove(self, query={}, collection='post'):

    self.db[collection].remove(query) 

  def update_one(self, update, query={}, collection='post'):

    result = self.db[collection].update_one(query, {'$set': update})
    return result.matched_count
