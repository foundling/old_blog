import pymongo

def find_by_key(db,**kwargs):
  print 'build a dict with kwargs here: \n', kwargs

def n_most_recent(db,n):
    '''
        n_most_recent n:int most recent published articles if n != 0. 
        Else, gets all articles.
    ''' 
    if n == 0:
      return db.posts.find({'published':True}).sort('date_published')[:]
    else: 
      return db.posts.find({'published':True}).sort('date_published')[:n]

class DB(object):
  '''
    has the mongo db connection bound to it
    some prefab query methods, not an orm
  '''
  def __init__(self, db_uri):
    self.db = pymongo.MongoClient(db_uri)

    self.n_most_recent = n_most_recent

def find_by_id(db, post_id):
  return db.posts.find_one({'post_id': post_id})
