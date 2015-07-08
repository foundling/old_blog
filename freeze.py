from flask.ext.frozen import Freezer
from blog import app

FREEZER_IGNORE_MIMETYPE_WARNINGS = True

freezer = Freezer(app)

if __name__ == '__main__':
  freezer.freeze()
