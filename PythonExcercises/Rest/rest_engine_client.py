'''
Created on Jan 16, 2016

@author: test
'''

import requests
import json

if __name__ == '__main__':

	def json_get(path='/'):
		r = requests.get('http://localhost:8080/' + path)
		print 'Status: %s' %r.status_code
		print 'Headers: %s' %r.headers
		if r.status_code == '200':
			print json.loads(r.content)
		else:
			print r.content
			
#json_get()
json_get('/')