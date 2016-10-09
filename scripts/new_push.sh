echo copying files to remote server ...

#rsync -auvP ../blog/build/ alex@138.68.49.132:/home/alex/alexramsdell.com/public_html --exclude=static 
rsync -auvP ../blog/build/ alex@138.68.49.132:/home/alex/alexramsdell.com/public_html --exclude=img 

echo done


#!/bin/bash

# Push all non-database changes to production server

#echo "cd'ing to /data/web"
#cd /data/web
#
#echo 'removing all pyc files'
#find  /data/web/blog -name '*.pyc' -delete
#
#
#if [ "$1" == "-n" ]
#then
#  echo 'mock syncing changes with the server ... (you passed the -n flag)'
#  rsync -auvnP --exclude={.DS_Store,*.swp,*.map,resize_all.sh,pushcontent.sh,db_exports,rsync_exclude.txt,*push.sh,*.pyc,.sass-cache,*.scss,.gitignore,db,.git,.etc,env,freeze.py,docs} /data/web/blog/ alexr@$box:/home/alexr/alexramsdell.com/ 
#else
#  rsync -auvP --exclude={.DS_Store,*.swp,resize_all.sh,*.map,pushcontent.sh,db_exports,rsync_exclude.txt,*push.sh,*.pyc,.sass-cache,*.scss,.gitignore,db,.git,.etc,env,freeze.py,docs} /data/web/blog/ alexr@$box:/home/alexr/alexramsdell.com/ 
#fi

