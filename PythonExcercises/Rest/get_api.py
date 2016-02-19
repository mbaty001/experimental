'''
Created on Jan 16, 2016

@author: test
'''
# http://search.safaribooksonline.com/book/programming/python/9781783980420/python-for-secret-agents/index_html?query=%28%28python+for+secret+agents%29%29#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE3ODM5ODA0MjAlMkZjaDAybHZsMnNlYzI5X2h0bWwmcXVlcnk9KChweXRob24lMjBmb3IlMjBzZWNyZXQlMjBhZ2VudHMpKQ==

''' SOCKET - file like object
open, read, close
'''

'''
GET - retrieve
	request.get
	request.get ( host, headers = {} )
	r.status_code
	r.headers
	r.content
POST - create
PUT - update
DELETE - delete
'''

''' python2.7 - module requests or urllib'''
''' python 3 - module http '''

import json
import requests

if __name__ == '__main__':

	api_key = '580c2a10f40a0b812aab4679b004d413'
	url = 'http://api.themoviedb.org/3/movie/popular'
	args = {'api_key' : api_key}

	r = requests.get(url, args)

	print json.loads(r.content)
