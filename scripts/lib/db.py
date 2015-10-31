import pymongo

class Database(object):

  def __init__(self, uri, db='blog'):
    self.db = pymongo.MongoClient(uri)[db]

  def find_one(self, collection='posts', **kwargs):
    query = dict([kw, kwargs[kw]] for kw in kwargs)
    return self.db[collection].find_one(query)

  def find_all(self, collection='posts', **kwargs):
    query = dict([kw, kwargs[kw]] for kw in kwargs)
    result_set = self.db[collection].find(query)
    return (result for result in result_set)

  def find_n_most_recent(self, n, collection='posts'):
    result_set = self.db[collection].find().sort('title', pymongo.DESCENDING)
    return (result for result in result_set)

if __name__ == '__main__':

  db = Database('mongodb://localhost:27017')
  print db.find_one(title="test")
  #for r in db.find_all(title="test"): print r
  #for r in db.find_n_most_recent(5): print r
