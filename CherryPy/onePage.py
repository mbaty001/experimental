#!/usr/bin/python

import cherrypy
import commands
import datetime
import jenkinsapi
import jira
import json
import os
import pyPdf
import pywapi
import re
import shelve
import StringIO
import unicodedata
import urllib

proxies = {'http' : 'http://global.proxy.lucent.com:8000' }

# HTML templates
_header = '''
	<html>
		<head>
			<title>One Page For All %s</title>			
			<meta http-equiv="refresh" content="600" >
		</head>
		<body>
			%s
			<center><h3>Michal One Page For All</h3></center>
			<div class="container">'''

_footer = '''
			</div>
		</body>
	</html>'''

_data_view = '''
	<br />
	<div>
		%s
	</div>'''

class Data():
	''' Data model '''

	ALU_HISTORY_LENGTH = 15
	CHF_HISTORY_LENGTH = 15
	TEMP_HISTORY_LENGTH = 15
	JENKINS_HISTORY_LENGTH = 15
	SHELVE_FILE = '/home/michal/Research/onePage/DB'
			
	def __init__(self):
		self.epaAluHistory = self.readHistory('epaAluHistory')
		self.chfHistory = self.readHistory('chfHistory')
		self.tempHistory = self.readHistory('tempHistory')
		self.jenkinsHistory = self.readHistory('jenkinsHistory')
		self.jenkins = self.setJenkinsResult(url = 'http://jenkins.host:port_number', 
								   jobName = 'jenkins_job_name')
		self.epaAlu = self.setALUStockQuote(symbol='EPA:ALU')
		self.chf = self.setCHFStock()
		self.soups = self.setSoups()
		self.weather = self.setWeather()
		self.myJira = self.setMyJiraIssues()

	def writeHistory(self, _historyName, _historyData):
		try:
			dbFile = shelve.open(Data.SHELVE_FILE)
			dbFile[_historyName] = _historyData
		except Exception, err:
			print str(err)
			sys.exit(1)
		finally:			
			dbFile.close()

	def readHistory(self, _historyName):
		try:
			dbFile = shelve.open(Data.SHELVE_FILE)
			retValue = dbFile[_historyName]
		except KeyError, err:
			retValue = list()
		except Exception, err:
			print str(err)
		finally:
			dbFile.close()

		return retValue				

	def setJenkinsResult(self, url, jobName):
		''' Retrieve Jenkins results for jobName '''
		print 'Retrieving Jenkins result from %s...' %(url)
		J = jenkinsapi.jenkins.Jenkins(url)

		job = J.get_job(jobName)

		bld = job.get_last_build()
		consoleOut = bld.get_console()

		total = passed = failed = 0

		for line in consoleOut.splitlines():
			m = re.match(r'(\d+) tests* total, (\d+) passed, (\d+) failed', line)
			if m:
				total += int(m.group(1))
				passed += int(m.group(2))
				failed += int(m.group(3))

		''' Divide by 2 since results are reported twice in the console output '''
		total /= 2
		passed /= 2
		failed /= 2	

		''' Set Jenkins history '''
		(self.jenkinsHistory, strHistory) = self.setHistory(self.jenkinsHistory, passed, Data.JENKINS_HISTORY_LENGTH, _oncePerDay = True)
		self.writeHistory('jenkinsHistory', self.jenkinsHistory)
		
		percentage = (100 * passed ) / total

		''' comment results '''		
		comment = ''
		color = 'Red'
		if percentage == 100:
			comment = 'Wow!!!'
			color = 'Green'
		elif percentage > 95:
			comment = 'Nice!'
			color = 'Light Green'
		elif percentage < 80:
			comment = 'Not good :('
		
		return ('<LI>Jenkins %s build: <a href="http://link_to_jenkins_results"><b>%s</b></a> Total: <b>%s</b> Passed: <b>%s (%s%s) </b> Failed: <b>%s</b> Duration: <b>%s</b> <b><font color="%s">%s</font></b> %s' % (jobName, jobName, bld.buildno, bld.buildno, total, passed, str(percentage), '%', failed, str(bld.get_duration()), color, comment , strHistory) )

	def getStockValue(self, symbol):
		''' Get symbol to PLN stoq '''
		url = 'http://stooq.pl/q/?s=%spln' % symbol
		print 'Retrieving cash stock value from %s...' %(url)
		out = urllib.urlopen(url, proxies = proxies).read()
		search = re.search(r'.id=aq_%spln_c5>(\d+)\.(\d+).' % symbol, out)
		value = float(search.group(1) + '.' + search.group(2))

		return value
		
	def setALUStockQuote(self, symbol):   
		''' Retrieve EPA:ALU stock value and calculate the cash amount in PLN from 423 options'''

		url = 'http://finance.google.com/finance/info?q=%s' % symbol
		print 'Retrieving ALU stock quote from %s...' %(url)
		lines = urllib.urlopen(url, proxies = proxies).read()[4:]
		''' make a list '''
		linesList = eval(lines)
		''' retrieve l_cur and remove encoding '''
		currentValue = linesList[0]['l_cur'][1:]

		(self.epaAluHistory, historyStr) = self.setHistory(self.epaAluHistory, currentValue, Data.ALU_HISTORY_LENGTH)	
		self.writeHistory('epaAluHistory', self.epaAluHistory)	

		euroValue = self.getStockValue('eur')
		''' compute the cash from options '''
		cash = (423 * (float(currentValue) - 1.893) - 35) * euroValue
						
		return ('<LI>EPA:ALU Current price: <b>%s</b>. Cash: <b>%.2f</b> PLN. %s' % (u'\u20AC' + currentValue, cash, historyStr))		

	def setHistory(self, _historyList, _currentValue, _historyLength, _oncePerDay = False):
		''' Make history list '''

		try:
			_lastValue = _historyList[len(_historyList) - 1][1]
		except IndexError:
			_lastValue = _currentValue

		if _currentValue > _lastValue:
			dot = 'green'
		elif _currentValue == _lastValue:
			dot = 'gray'
		else:
			dot = 'red'

		''' Add only once per day if _oncePerDay is True '''
		if _oncePerDay:
			found = False
			today = datetime.datetime.now().strftime('%Y.%m.%d')
			for entry in _historyList:
				if today in entry:
					found = True
					break
			if not found:
				_historyList.append([dot, _currentValue, today])
		else:			
			_historyList.append([dot, _currentValue])

		if len(_historyList) > _historyLength :
			_historyList = _historyList[1:]

		historyStr = 'History: '
		for history in _historyList:
			historyStr += ' <b><font color="%s">&diams;</font></b> ' %(history[0])

		return (_historyList, historyStr)

	def setCHFStock(self):
		''' Retrieve CHF average value '''
		chfValue = self.getStockValue('chf')

		(self.chfHistory, historyStr) = self.setHistory(self.chfHistory, chfValue, Data.CHF_HISTORY_LENGTH)
		self.writeHistory('chfHistory', self.chfHistory)

		return ('<LI>CHF Current price: <b>%s</b> %s' %(chfValue, historyStr))
		
	def setSoups(self):
		''' retrieve soups from sodexo '''
	
		pdfFile = '/tmp/jadlospis.pdf'		
		txtFile = '/tmp/jadlospis.txt'	
		today = datetime.datetime.now().strftime('%Y.%m.%d')

		print "Retrieving Sodexo's soups..."
		menu = urllib.urlopen('http://address_of_cantine/stolowka/jadlospis.pdf', proxies = proxies).read()

		''' Retrieve jadlospis.pdf and save it to the disk '''
		with open(pdfFile, 'wb') as fHandler:
			fHandler.write(menu)

		''' Convert pdf to txt. This needs to be improved to make it platform independent. '''
		rc, out = commands.getstatusoutput('/usr/bin/pdftotext %s %s' % (pdfFile, txtFile))
		if rc != 0:
			print out
			sys.exit(1)

		''' Check if there are current date in txtFile'''
		with open(txtFile, 'r') as fHandler:
			out = fHandler.read()			
			if not re.search(r'%s' %(today), out):
				''' cleanup '''
				print 'No data for %s' %(today)
				print out
				os.remove(pdfFile)
				os.remove(txtFile)
				return '<LI>Sodexo soups: <b> NO DATA AVAILABLE</b>'		

		''' Retrieve soups '''
		begin = False
		days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
		next = 0
		soupDict = {'Monday' : [], 'Tuesday' : [], 'Wednesday' : [], 'Thursday' : [], 'Friday' : [] }
		with open(txtFile, 'r') as fHandler:
			for line in fHandler:
				line = line.strip('\n')
				if line.startswith('ZUPY'):
					begin = True
					continue
				if line.startswith('DANIA'):
					break				
				if begin and line != '':					
					soupDict[days[next]].append(line)
					next = (next + 1) % 5;

		now = datetime.datetime.now().strftime('%A')
		try:
			tomorrow = days[days.index(now) + 1]
			tomorrowStr = ' tomorrow (%s): <b>%s</b> or <b>%s</b>' %(tomorrow, soupDict[tomorrow][0], soupDict[tomorrow][1])
		except IndexError, err:
			tomorrowStr = ''
			pass
		
		''' cleanup '''
		os.remove(pdfFile)
		os.remove(txtFile)
		
		try:
			retStr = '<LI>Sodexo soups for %s: <b>%s</b> or <b>%s</b> %s' % (now, soupDict[now][0], soupDict[now][1], tomorrowStr)
		except IndexError, err:
			retStr = '<LI>Sodexo soups for %s: <b>%s</b> or <b>%s</b> %s' % (now, 'None', 'None', tomorrowStr)

		return retStr

	def setWeather(self):
		''' get weather from yahoo.com for Torun: PLXX0028 '''
		print "Retrieving Yahoo's weather..."
		result = pywapi.get_weather_from_yahoo('PLXX0028', 'metric')

		(self.tempHistory, historyStr) = self.setHistory(self.tempHistory, result['condition']['temp'], Data.TEMP_HISTORY_LENGTH)
		self.writeHistory('tempHistory', self.tempHistory)

		return ('<LI>Forecast for Torun. Day: %s - %s. Preassure: %s. Condition: %s. Temp: <b>%s</b>. %s' %(result['astronomy']['sunrise'], result['astronomy']['sunset'], result['atmosphere']['pressure'], result['condition']['text'], result['condition']['temp'], historyStr))

	def setMyJiraIssues(self):
		''' get my jira issues '''
		retStr = '<LI>My JIRA issues: '

		print 'Retrieving JIRA issues...'
		options = { 'server' : 'https://jira_address' }
		j = jira.client.JIRA(options, basic_auth = ('jira_user', 'jira_passwd'))
		issues = j.search_issues('assignee=jira_user AND resolution = Unresolved ORDER BY updatedDate DESC')
		
		if len(issues) != 0:
			retStr += '<UL type="CIRCLE">'
			for issue in issues:
				retStr += '<LI><a href="https://jira_address/%s"><b>%s</b> : %s</a>' %(issue.key, issue.key, issue.fields.summary)
			retStr += '</UL>'
		else:
			retStr += '<b>None</b>'
			
		return retStr
		

	def refresh(self, refreshAll):
		''' Refresh only the values which may change during the day '''
		self.epaAlu = self.setALUStockQuote(symbol='EPA:ALU')
		self.chf = self.setCHFStock()
		self.weather = self.setWeather()

		if refreshAll:
			''' Refresh the rest of data too '''
			self.jenkins = self.setJenkinsResult(url = 'http://jenkins_server:port', 
						   jobName = 'job_name')
			self.myJira = self.setMyJiraIssues()
			self.soups = self.setSoups()

class OnePageApp():
	''' CherryPy application '''
	def __init__(self):
		self.page = list()
		self.data = Data()
		self.hour = datetime.datetime.now().hour
		self.refreshAll = False

	@cherrypy.expose
	def index(self):

		''' if hour changed from 5 to 6 - refresh all the data'''
		cHour = datetime.datetime.now().hour
		refreshDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

		if cHour == 6 and self.hour != cHour:
			self.hour = cHour
			self.refreshAll = True
		else:
			self.refreshAll = False
			
		self.data.refresh(self.refreshAll)

		self.page = [_header %(refreshDate, refreshDate)]
		
		''' Add all attributes of data class instance '''
		self.page.append(_data_view %(self.data.epaAlu))	
		self.page.append(_data_view %(self.data.chf))
		self.page.append(_data_view %(self.data.weather))
		self.page.append(_data_view %(self.data.jenkins))
		self.page.append(_data_view %(self.data.soups))
		self.page.append(_data_view %(self.data.myJira))			

		self.page.append(_footer)

		return self.page
			

def main():
	''' define global configuration of CherryPy '''
	global_conf = {
		'global' : { 'engine.autoreload.on' : True, 
					 #'server.socket_host' : '127.0.0.1', 
					  'server.socket_host' : 'host_name',	
					 'server.socket_port' : port,
			}
	}

	cherrypy.config.update(global_conf)
	
	onePage = OnePageApp()
	
	cherrypy.tree.mount(onePage, '/', )

	cherrypy.engine.start()
	cherrypy.engine.block()
	
if __name__ == '__main__':
	main() 