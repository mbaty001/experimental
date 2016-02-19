'''
Created on Jan 16, 2016

@author: test
'''
# http://search.safaribooksonline.com/book/programming/python/9781783980420/python-for-secret-agents/index_html?query=%28%28python+for+secret+agents%29%29#X2ludGVybmFsX0h0bWxWaWV3P3htbGlkPTk3ODE3ODM5ODA0MjAlMkZjaDAybHZsMnNlYzI5X2h0bWwmcXVlcnk9KChweXRob24lMjBmb3IlMjBzZWNyZXQlMjBhZ2VudHMpKQ==

''' SOCKET - file like object
open, read, close
'''

'''
GET
	request.get
	r.status_code
	r.headers
	r.content
POST
PUT
DELETE
'''

''' python2.7 - module requests or urllib'''
''' python 3 - module http '''

import httplib
import requests

if __name__ == '__main__':
	
	path_list = [
    "/wikipedia/commons/7/72/IPhone_Internals.jpg",
    "/wikipedia/en/c/c1/1drachmi_1973.jpg",
	]

	host = 'http://upload.wikimedia.org'
	
	''' need to open a browser to make it works '''
	for path in path_list:
		r = requests.get(host + path, headers = {'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53'})
		print 'Status: %s ' %r.status_code
		print 'Headers: %s' %r.headers
		file_name = path.split('/')[-1]
		with open(file_name, 'wb') as image:
			image.write(r.content)
	
