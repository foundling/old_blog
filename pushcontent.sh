#!/bin/bash

# push only database changes to server
# export current, send to the server, drop those tables, import from my newly exported json array files

if [ "$1" == "-n" ]
then
  echo 'testing changes, you passed -n flag'
  rsync -auvnP db_exports/{posts,static,projects} alexr@$box:/home/alexr/alexramsdell.com/db_exports
else
  echo 'syncing local mongo databses with production server'
rsync -auvP db_exports/{posts,static,projects} alexr@$box:/home/alexr/alexramsdell.com/db_exports
ssh alexr@$box "cd /home/alexr/alexramsdell.com/db_exports && sh update_db.sh"
fi
