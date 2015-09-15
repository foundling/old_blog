def n_most_recent(db,n):
    ''' n most recent published articles ''' 
    return db.posts.find({'published':True}).sort('date_published')[:n]

