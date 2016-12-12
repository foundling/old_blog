THEME="$1"

if [ -z "$1" ]
then
    THEME='default'
fi

. env/bin/activate

mongod --dbpath=app/db >/dev/null &
THEME=$THEME python start.py
