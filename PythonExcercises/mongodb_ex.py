#!/usr/bin/env python

'''
Start mangodb
 cd /cygdrive/d/Research/MongoDB/mongodb-win32-i386-2.0.0/bin
 ./mongod.exe --dbpath ../../data/db
 
 mango <-- start shell
 1. create db:
  use michal <-- mango will not create a db permament until you insert a data there
  db <-- list current db
  i = {'author' : 'John Cook'}
  j = {'author' : 'Ali Baba'}
  db.testData.insert(i) <-- insert a data into db michal
  db.testData.insert(j)
'''
import pymongo
import argparse
import sys

class DB(object):
    ''' Generic class for handling MongoDB '''
    
    def __init__(self, db, host='localhost', port=27017):
        self.host = host
        self.port = port
        self.client = pymongo.MongoClient(self.host, self.port)
        self.db = self.client[db]
        self.collections = self.db.collection_names() if not None else None
      
    def getDb(self):        
        return self.db
    
    def getCollections(self):
        return self.collections
    
    def checkCollection(self, collection):
        return collection in self.collections
    
    def getAllData(self, collection):
        try:    
            return self.db[collection].find()
        except Exception, err:
            print 'getAllData: Cannot get any data (%s)' %err
            sys.exit(1)
    
    def getData(self, collection, key, value):
        try:
            return self.db[collection].find_one({key : value})
        except Exception, err:
            print 'getData: Cannot get any data (%s)' %err
            sys.exit(1)       
    
def parseArgs():
    parser = argparse.ArgumentParser( description='MongoDB training', formatter_class=argparse.ArgumentDefaultsHelpFormatter )
 
    parser.add_argument( '--host', action='store', default='localhost', help='MongoDB host' )
    parser.add_argument( '--port', action='store', default=27017, help='MongoDB port')

    return vars(parser.parse_args())

if __name__ == '__main__':
    args = parseArgs()
    
    client = DB(host=args['host'], port=args['port'], db='michal')                  
    print client.getCollections()
    
    print client.checkCollection('testData')
    
    alldata = client.getAllData('testData')
    print alldata
    
    onedata = client.getData('testData', 'author', 'John Cook')
    print onedata 
        
    