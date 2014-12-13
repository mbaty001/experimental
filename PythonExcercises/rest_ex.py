'''
Read data from film db via REST API.
themoviedb.apiary.io
https://www.themoviedb.org/documentation/api
http://docs.python-requests.org/en/latest/user/quickstart/

'''

import json
import requests

key = '580c2a10f40a0b812aab4679b004d413'

if __name__ == '__main__':
        
    args = {'api_key' : key, 'query' : 'commando'}
    r = requests.get('http://api.themoviedb.org/3/search/tv', params = args) 
    print r.json()
    
    args = {'api_key' : key}
    r = requests.get('http://api.themoviedb.org/3/configuration', params= args)
    for k, v in r.json().iteritems():
        print 'KEY: %s' %k
        print 'VALUE: %s' %v
        
    