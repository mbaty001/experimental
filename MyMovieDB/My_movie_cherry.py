#!/usr/bin/python

import os
import cherrypy
import My_movie_db

# HTML templates
_header = '''
	<html>
		<head>
			<title>THE MOST POPULAR RECENT MOVIES</title>
			 <link href="/static/css/style.css" rel="stylesheet">	
		</head>
		<body>
			<center><h3>THE MOST POPULAR RECENT MOVIES</h3></center>
			<div class="container">
			<table>
			<tr><th>POPULARITY</th><th>VOTE</th><th>TITLE</th><th>PRODUCTION</th><th>GENRE</th><th>POSTER</th><th>OVERVIEW</th></tr>'''			

_footer = '''
			</table border="1">
			</div>
		</body>
	</html>'''

_data_view = '''
	<tr>
		<td>%(popularity)s</td>
		<td>%(vote_average)s</td>
		<td><b>%(title)s</b></td>
		<td>%(production_countries)s</td>
		<td>%(genres)s</td>		
		<td><img src="https://image.tmdb.org/t/p/w130/%(poster_path)s" alt="%(title)s" height="130" width="100"/></td>
		<td>%(overview)s</td>
	</tr>'''
		
class MyMovieDB(object):
		
	def __init__(self):
		self.db = My_movie_db.MovieDB()
		self.page = list()
		
	@cherrypy.expose
	def index(self):
		self.page = [_header]
		map(lambda x: self.page.append(_data_view %(x)), self.db.populars)
		self.page.append(_footer)
		return self.page
	
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