import pymongo

class Database(object):

  def __init__(self, uri, db='blog'):
    self.db = pymongo.MongoClient(uri)[db]

  def find_one(self, collection='posts', **kwargs):
    query = dict([kw, kwargs[kw]] for kw in kwargs)
    print self.db[collection].find_one(query)

if __name__ == '__main__':

  db = Database('mongodb://localhost:27017')
  db.find_one(title='What\'s the Difference Between a Good Joke and a Great Joke?')
