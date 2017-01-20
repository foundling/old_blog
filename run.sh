THEME="$1"

. env/bin/activate

echo 'starting mongod and sending to bg ... [run sh stop.sh to kill it]'
mongod --dbpath=app/db >/dev/null &

echo 'opening a server on localhost ... '

python start.py &
open -a /Applications/Google\ Chrome.app http://localhost:5000

