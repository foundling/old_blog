import os
import sys
import pymongo

from config import config


def connect(host='localhost',port='27017'):

    serverIsRunning = os.system('pgrep -q mongod') == 0

    if not serverIsRunning:
        print 'mongod server is not running. start it and run the script again'
        return False

    try:
        client = pymongo.MongoClient(''.join([
                                        'mongodb://',
                                        host,
                                        ':',
                                        port,
                                        '/',
                                        ]),
                                        connectTimeoutMS=1000
                                     )
    except pymongo.errors.ConnectionFailure:
        return False

    print 'MongoDB server is *probably* running :]'
    return client

def print_config_values():

    print 'CONFIG VALUES:'
    for val in config:
        print '{} => {}'.format(val, config[val])
    print ''


