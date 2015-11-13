#!/bin/bash

# push only database changes to server
# export current, send to the server, drop those tables, import from my newly exported json array files


RHOST=104.131.106.239

# SET VARS FOR DRYRUN
if [ "$1" == "-n" ]
then
  DRYRUN="n"
  TESTPREFIX="[ MOCK (you passed the -n flag) ] "
fi

# IF DRY RUN, RUN RSYNC WITH N FLAG
if [ -n "$DRYRUN" ]
then 
  echo $TESTPREFIX "Syncing local mongo databses with production server"
  rsync -auvP$DRYRUN db_exports/{posts,static,projects} alexr@$RHOST:/home/alexr/alexramsdell.com/db_exports/
  exit 0
fi

# DO THE COMMAND FOR REAL
if [ $(pgrep mongod) ]
then
  echo "Syncing local mongo databses with production server"

  # export mongodb collections from blog to db_exports
  for i in {projects,posts,static}
  do 
    mongoexport -d blog -c $i --type json --jsonArray > db_exports/$i
  done

  # rsync them to remote host
  rsync -auvP db_exports/{posts,static,projects} alexr@$RHOST:/home/alexr/alexramsdell.com/db_exports/

  # run update script on remote host
  ssh alexr@$RHOST "cd /home/alexr/alexramsdell.com/db_exports && sh update_db.sh"
  exit 0
else
  echo 'error: mongod is not running. Start it and try again.'
  exit 1
fi
