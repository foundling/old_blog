from flask.ext.frozen import Freezer
from blog import application

FREEZER_IGNORE_MIMETYPE_WARNINGS = True
FREEZER_BASE_URL = '/data/web/blog'

freezer = Freezer(application)

if __name__ == '__main__':
    freezer.freeze()
