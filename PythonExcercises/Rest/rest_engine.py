'''
Created on Jan 16, 2016

@author: test
'''

'''
 POST - create //host/app/blog
 GET - retrieve (search) //host/app/blog/?title="Any title" - multiple objects
 GET - retrieve (instance) //host/app/bldg/id - single object
 PUT - update //host/app/blog/id
 DELETE - delete //host/app/blog/id
 
 code responses:
 	200 - OK
 	201 - created
 	204 - no content 
 	400 - bad request
 	401 - unauthorized
 	404 - not found
 	
 	2xx - success
 	4xx - errors
 	
 	HTTP is stateless - no provision for login and logodd - each request must be separately authenticated 
 		Authorization header to provide login and passwd - with SSL - or use tokens
 
'''

import random
import sys
import wsgiref.util
import json
from wsgiref.simple_server import make_server

class Wheel(object):
    """Abstract, zero bins omitted."""
    def __init__( self ):
        self.rng= random.Random()
        self.bins= [
            {str(n): (35,1),
            self.redblack(n): (1,1),
            self.hilo(n): (1,1),
            self.evenodd(n): (1,1),
            } for n in range(1,37)
        ]
    @staticmethod
    def redblack(n):
        return "Red" if n in (1, 3, 5, 7, 9,  12, 14, 16, 18,
            19, 21, 23, 25, 27,  30, 32, 34, 36) else "Black"
    @staticmethod
    def hilo(n):
        return "Hi" if n >= 19 else "Lo"
    @staticmethod
    def evenodd(n):
        return "Even" if n % 2 == 0 else "Odd"
    def spin( self ):
        return self.rng.choice( self.bins )
       
class Zero(Wheel):
    def __init__( self ):
    	Wheel.__init__(self)    	
        self.bins += [ {'0': (35,1)} ]

class DoubleZero(Zero):
    def __init__( self ):   
    	Zero.__init__(self)     
        self.bins += [ {'00': (35,1)} ]
        
class American( DoubleZero):
    pass

class European( Zero):
    pass
   
if __name__ == '__main__':
	
	european = European()
	american = American()
	
	def wheel(environ, start_response):
	    request= wsgiref.util.shift_path_info(environ) # 1. Parse.
	    print >> sys.stderr, "wheel %s" %request # 2. Logging.
	    if request.lower().startswith('eu'): # 3. Evaluate.
	        winner= european.spin()
	    else:
	        winner= american.spin()
	    status = '200 OK' # 4. Respond.
	    headers = [('Content-type', 'application/json; charset=utf-8')]
	    start_response(status, headers)
	    return [ json.dumps(winner).encode('UTF-8') ]
	   
	def roulette_server(count=1):
	    httpd = make_server('', 8080, wheel)
	    if count is None:
	        httpd.serve_forever()
	    else:
	        for c in range(count):
	            httpd.handle_request()

roulette_server(count=None)