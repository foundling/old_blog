echo 'exporting database tables to db_exports ... '

for i in {projects,posts,static}
do
    mongoexport -d blog -c $i --type json --jsonArray > db_exports/$i
done

