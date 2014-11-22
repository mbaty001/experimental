#!/usr/bin/env python

import pymongo
import argparse

def parseArgs():
    parser = argparse.ArgumentParser( description='MongoDB training', formatter_class=argparse.ArgumentDefaultsHelpFormatter )
 
    parser.add_argument( '--host', action='store', default='localhost', help='MongoDB host' )
    parser.add_argument( '--port', action='store', default=27017, help='MongoDB port')

    return vars(parser.parse_args())

if __name__ == '__main__':
    args = parseArgs()
    
    client = pymongo.MongoClient(args['host'], args['port'])
    
    print client
