'''
Read data from film db via REST API.
themoviedb.apiary.io
https://www.themoviedb.org/documentation/api
http://docs.python-requests.org/en/latest/user/quickstart/

'''

import json
import requests

def print_json(what):        
    print json.dumps(what, sort_keys=True, indent=4, separators=(',', ':'))

class MovieDB(object):
    def __init__(self):
        self.api_key = '580c2a10f40a0b812aab4679b004d413'
        self.url = 'http://api.themoviedb.org/3'
        self.args = {'api_key' : self.api_key}
        self.popular = Request(self.url + '/movie/popular', self.args).get()['results'] or None
        
    def get_movie(self, id):      
        print_json(Request(self.url + '/movie/%s' %id, self.args).get())
        "https://image.tmdb.org/t/p/w130/<poster_path>"
        

class Request(object):
    def __init__(self, url, params):
        self.url= url
        self.params = params
        
    def get(self):
        _request = requests.get(self.url, params = self.params)
        return _request.json()    

if __name__ == '__main__':
        
    db = MovieDB()
    for movie in db.popular:
        db.get_movie(movie['id'])
        print 30*'*' 

    