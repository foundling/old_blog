#!/bin/bash

# Push all non-database changes to production server

echo "cd'ing to /data/web"
cd /data/web

echo 'removing all pyc files'
find  /data/web/blog -name '*.pyc' -delete


if [ "$1" == "-n" ]
then
  echo 'mock syncing changes with the server ... (you passed the -n flag)'
  rsync -auvnP --exclude={pushcontent.sh,db_exports,rsync_exclude.txt,*push.sh,*.pyc,.sass-cache,*.scss,.gitignore,db,.git,.etc,env,freeze.py,docs} /data/web/blog/ alexr@$box:/home/alexr/alexramsdell.com/ 
else
  rsync -auvP --exclude={pushcontent.sh,db_exports,rsync_exclude.txt,*push.sh,*.pyc,.sass-cache,*.scss,.gitignore,db,.git,.etc,env,freeze.py,docs} /data/web/blog/ alexr@$box:/home/alexr/alexramsdell.com/ 
fi

