THEME="$1"

if [ -z "$1" ]
then
    THEME='default'
fi

. env/bin/activate

mongod --dbpath=app/db >/dev/null &
echo $THEME
open -a /Applications/Google\ Chrome.app http://localhost:5000
THEME=$THEME python start.py
