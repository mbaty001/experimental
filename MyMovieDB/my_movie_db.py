'''
Read data from film db via REST API.
themoviedb.apiary.io
https://www.themoviedb.org/documentation/api
http://docs.python-requests.org/en/latest/user/quickstart/

'''

import json
import requests

class MovieDB(object):
    def __init__(self):
        self.api_key = '580c2a10f40a0b812aab4679b004d413'
        self.url = 'http://api.themoviedb.org'
        
    def get_configuration(self):        
        url = self.url + '/3/configuration'
        args = {'api_key' : self.api_key}
        return Request(url, args).get()
    
    def print_configuration(self):
        config = self.get_configuration()
        print json.dumps(config, sort_keys=True, indent=4, separators=(',', ':'))

class Request(object):
    def __init__(self, url, params):
        self.url= url
        self.params = params
        
    def get(self):
        _request = requests.get(self.url, params = self.params)
        return _request.json()    

if __name__ == '__main__':
        
    db = MovieDB()
    db.print_configuration()
    