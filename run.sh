mkdir -p app/db
mongod --dbpath=app/db &
. env/bin/activate
THEME='new' python start.py
