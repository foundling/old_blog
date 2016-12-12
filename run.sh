THEME="$1"

. env/bin/activate
mongod --dbpath=app/db &
THEME=( THEME || 'default') python start.py
