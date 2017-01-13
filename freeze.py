from flask.ext.frozen import Freezer
from app import blog

FREEZER_IGNORE_MIMETYPE_WARNINGS = True
FREEZER_DESTINATION='/data/web/blog/build'
FREEZER_BASE_URL = '/data/web/blog'

freezer = Freezer(blog)

if __name__ == '__main__':
    freezer.freeze()
