#!/usr/bin/python

import sys
import argparse

def argParse():

    parser = argparse.ArgumentParser( description='Your description', formatter_class=argparse.ArgumentDefaultsHelpFormatter )

    parser.add_argument( '-m', '--mode', action='store', default='write', choices=['append', 'write'], help='help message' )
    parser.add_argument( '-o', '--operation', action='store', default='all', choices=['add', 'delete', 'modify', 'all'], help='help message' )
    parser.add_argument( '-a', '--attrs', metavar='ATTR_FILE', required='True', help='help message')
    parser.add_argument( '-f', '--file', metavar='XML_FILE', required='True', help='help message' )
    parser.add_argument( '-d', '--debug', action='store_true', default='False' )

    return vars(parser.parse_args())

if __name__ == '__main__':
    args = argParse()
    print args
