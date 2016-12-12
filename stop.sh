proc=`pgrep mongod`

if test $proc
then
    echo killing mongod
    sudo kill -9 $proc
    echo done
else
    echo no mongodb process to kill 
fi

