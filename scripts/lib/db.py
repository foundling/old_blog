import pymongo
import sys
import os

class Database(object):

  def __init__(self, uri, db_name='blog'):

    self.db = self.connect(uri).blog


  def connect(self,uri):

      ''' returns client or exits '''

      server_running = os.system('pgrep -q mongod') == 0

      if not server_running:
          print 'The mongod server is not running. Try starting it and run the script again'
          sys.exit(1)

      try:
          client = pymongo.MongoClient(uri, connectTimeoutMS=1000)

      except pymongo.errors.ConnectionFailure:
          print 'could not connect to the database'
          sys.exit(1)

      return client


  def find_one(self, query, collection='posts'):
    return self.db[collection].find_one(query)

  def find_all(self, query, collection='posts'):
    result_set = self.db[collection].find(query)
    return (result for result in result_set)

  def find_n_most_recent(self, n, collection='posts'):
    result_set = self.db[collection].find().sort('title', pymongo.DESCENDING)
    return (result for result in result_set)

  def update_one(self, query, update, collection='posts'):
    ''' 
      note, this uses $set to update one or more fields without replacing entire doc 
      user passes in objects
    '''

    result = self.db[collection].update_one(query, update)
    return result.matched_count

if __name__ == '__main__':

  db = Database('mongodb://localhost:27017')

  #print db.update_one({'title':'test updated!'},{'$set' : {'title':'test updated again!'}})
  #print db.find_one(title='test updated again!')
  #for r in db.find_all(title="test"): print r
  #for r in db.find_n_most_recent(5): print r
