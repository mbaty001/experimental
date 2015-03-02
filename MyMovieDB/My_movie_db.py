'''
Read data from film db via REST API.
themoviedb.apiary.io
https://www.themoviedb.org/documentation/api
http://docs.python-requests.org/en/latest/user/quickstart/

'''

import json
import operator
import requests

def print_json(what):        
    print json.dumps(what, sort_keys=True, indent=4, separators=(',', ':'))

class MovieDB(object):
    def __init__(self):
        self.api_key = '580c2a10f40a0b812aab4679b004d413'
        self.url = 'http://api.themoviedb.org/3'
        self.args = {'api_key' : self.api_key}
        self.populars = Request(self.url + '/movie/popular', self.args).get()['results'] or None
        self.populars = map(lambda x: self.get_movie(x['id']), self.populars)
        self.sorted_populars_by('popularity')
        
    def sorted_populars_by(self, what):
        self.populars = sorted(self.populars, 
                               key=operator.itemgetter(what),
                               reverse = True)    
            
    def get_movie(self, id):      
        dataDict = Request(self.url + '/movie/%s' %id, self.args).get()        
        return {'title' : dataDict['title'], 
               'vote_average' : dataDict['vote_average'], 
               'production_countries' : ', '.join(map(lambda x: x['name'], dataDict['production_countries'])), 
               'poster_path' : 'https://image.tmdb.org/t/p/w130/' + dataDict['poster_path'],
               'overview' : dataDict['overview'], 
               'genres' : ', '.join(map(lambda x: x['name'], dataDict['genres'])),
               'popularity' : round(dataDict['popularity'], 2)}
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
     
    for movie in db.populars:
        print db.get_movie(movie['id'])
        print 30*'*' 

    