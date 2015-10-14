def n_most_recent(db,n):
    ''' n_most_recent - gets n most recent published articles if n != 0. Else, gets all articles.''' 
    if n == 0:
      return db.posts.find({'published':True}).sort('date_published')[:]
    else: 
      return db.posts.find({'published':True}).sort('date_published')[:n]

def findById(id):
  return db.posts.find({'_id',ObjectId(id)})

      
