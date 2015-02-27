#!/usr/bin/python

import os
import cherrypy
import My_movie_db

# HTML templates
_header = '''
	<html>
		<head>
			<title>My movie db</title>
			 <link href="/static/css/style.css" rel="stylesheet">	
		</head>
		<body>
			<center><h3>My movie db</h3></center>
			<div class="container">
			<table>'''			

_footer = '''
			</table border="1">
			</div>
		</body>
	</html>'''

_data_view = '''
	<tr>
		<td>%(title)s</td>
	</tr>'''
		
class MyMovieDB(object):
		
	def __init__(self):
		self.db = My_movie_db.MovieDB()
		self.page = list()
		
	def index(self):
		self.page = [_header]
		map(lambda x: self.page.append(_data_view %(x)), self.db.populars)
		self.page.append(_footer)
		return self.page
	index.exposed = True
	
if __name__ == '__main__':
	
	conf = {
		'/' : {
			'tools.staticdir.root' : os.path.abspath(os.getcwd())
			},
		'/static' : {
			'tools.staticdir.on' : True,
			'tools.staticdir.dir' : '.\\static'
			}
		}
	
	cherrypy.config.update({'server.socket_port' : 8081})
	cherrypy.quickstart(MyMovieDB(), '/', conf)