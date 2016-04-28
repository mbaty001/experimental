#!/usr/bin/python

from globals import *
from sqlite3 import *
import pexpect
import sys
import logging
import threading

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG, filename='suDetective.log')
#logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
	
class MyLog(logging.getLoggerClass()):
	def __init__(self, _lab):
		self._lab = _lab
		self.spaces = 11 - len(self._lab)
		
	def debug(self, _msg):
		
		logging.debug(self._lab.upper() + ' '*self.spaces + ': ' + _msg)
		
	def info(self, _msg):
		logging.info(self._lab.upper() + ' '*self.spaces + ': ' + _msg)
		
class TimeoutReached(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class SUDetective(threading.Thread):
	def __init__(self, lab, log):
		threading.Thread.__init__(self)
		self.lab = lab
		self.log = log

	def runCmd(self, _child, _cmd, _prompt):
		self.log.debug(str(_cmd))
		_child.sendline(_cmd)
		_rc = _child.expect([_prompt, pexpect.TIMEOUT])
		if _rc == 1:
			raise TimeoutReached('TIMEOUT reached - ' + str(_cmd))
		return _child.before.splitlines()[1:]
		
	def getHwType(self, hwType):
		if hwType == 'SUNW,Netra-240': return 'N240'
		elif hwType == 'SUNW,Netra-T5220': return 'T5220'
		elif hwType == 'x86_64': return 'ACSCG'
		elif hwType == 'SUNW,Ultra-80': return 'N1400'
		elif hwType == 'CG2100': return 'TSCG'
		elif hwType == 'INTELMHT_2x2.3GHZ': return 'MHT'
		elif hwType == 'FORCE745_1x1.6GHZ': return 'PM'
		elif hwType == 'INTEL5504_1x1.0GHZ': return 'PIII'
		elif hwType == 'CG2100_SSD': return 'MSCG'
		elif hwType == 'INTELLHT_2x2.8GHZ': return 'LHT'
		elif hwType == 'HPCC2300_2x1.2GHZ': return 'HP'
		elif hwType == 'INTELCHESNEE_1x3.0GHZ': return 'IC'
		else: return

	def getLabIdByData(self, connection, name, noOfLangs, hap, rms, dualIp, acsHwId, ipTypeId):
		connection.execute(''' SELECT  idLAB from LAB WHERE
                  NAME = ? AND NO_OF_LANGS = ? AND HAP = ?
                  AND RMS = ? AND DUAL_IP = ? AND ACS_TYPE_idHW_TYPE = ?
                  AND IP_TYPE_idIP_TYPE = ?''', (name, noOfLangs, hap, rms, dualIp, acsHwId, ipTypeId))

		labData = connection.fetchone()
		if labData == None:
			return None
		else:
			return labData[0]

	def getHwIdByName(self, connection, name):
		connection.execute(''' SELECT idHW_TYPE FROM HW_TYPE WHERE NAME=?''', (name,))
		return connection.fetchone()[0]

	def getIpIdByName(self, connection, name):
		connection.execute(''' SELECT idIP_TYPE FROM IP_TYPE WHERE NAME=?''', (name,))
		return connection.fetchone()[0]
	
	def getSuIdByName(self, connection, name):
		connection.execute('''SELECT idSU_TYPE FROM SU_TYPE WHERE NAME = ?''', (name,))
		return connection.fetchone()[0]

	def getNodeTypeIdByName(self, connection, name):
		connection.execute('''SELECT idNODE_TYPE FROM NODE_TYPE WHERE NAME = ?''', (name,))
		return connection.fetchone()[0]
	
	def getSuStateIdByName(self, connection, name):
		connection.execute(''' SELECT idSU_STATE FROM SU_STATE WHERE NAME = ?''', (name,))
		return connection.fetchone()[0]
		
	def addLab(self, connection, name, noOfLangs, hap, rms, dualIp, acsHwId, ipTypeId):
		# Check if given lab already exists
		labId = self.getLabIdByData(connection, name, noOfLangs, hap, rms, dualIp, acsHwId, ipTypeId)
		if labId == None:
			self.log.info('Adding new lab (' + name + ')...')
			connection.execute(''' INSERT INTO LAB (NAME, NO_OF_LANGS, HAP, RMS, DUAL_IP, ACS_TYPE_idHW_TYPE, IP_TYPE_idIP_TYPE) 
					VALUES (?, ?, ?, ?, ?, ?, ?) ''', (name, noOfLangs, hap, rms, dualIp, acsHwId, ipTypeId))

			# Get the lab id
			labId = self.getLabIdByData(connection, name, noOfLangs, hap, rms, dualIp, acsHwId, ipTypeId)

		else:
			self.log.debug('LAB ID: ' + str(labId))
			self.log.debug('Lab ' + name + ' already added.')
	
		return labId

	def getMsIdByData(self, connection, labId, hwTypeId, ms):
		connection.execute(''' SELECT  idMS from MS WHERE NAME = ? AND MS_TYPE_idHW_TYPE = ?
                    AND LAB_idLAB = ?''', (ms, hwTypeId, labId))

		msId = connection.fetchone()
		if msId == None:
			return None
		else:
			return msId[0]

	def getTsIdByData(self, connection, labId, hwTypeId, ts):
		connection.execute(''' SELECT  idTS from TS WHERE NAME = ? AND TS_TYPE_idHW_TYPE = ?
                      AND LAB_idLAB = ?''', (ts, hwTypeId, labId))

		tsId = connection.fetchone()
		if tsId == None:
			return None
		else:
			return tsId[0]
			
	def getSuIdByData(self, connection, suType, labId, suFrom, suTo, suStartTime, suEndTime, suStateId):
		connection.execute('''SELECT idSU FROM SU WHERE SU_TYPE_idSU_TYPE = ? AND LAB_idLab  = ?
					AND SU_FROM = ? AND SU_TO = ? AND SU_START_TIME = ? 
					AND SU_END_TIME = ? AND SU_STATE_idSU_STATE = ?''', (suType, labId, suFrom, suTo, suStartTime, suEndTime, suStateId))
		idSu = connection.fetchone()		
		if idSu == None:
			return None
		else:
			return idSu[0]

	def getLogIdByData(self, c, hwId, nodeTypeId, suId, logFile, node):
		c.execute(''' SELECT idSU_LOG FROM SU_LOG WHERE HW_TYPE_idHW_TYPE  = ?
					AND NODE_TYPE_idNODE_TYPE = ? AND SU_idSU = ? AND
					LOG_FILE = ? AND NODE_NAME = ?''', (hwId, nodeTypeId, suId, logFile, node))
		idLab = c.fetchone()
		if idLab == None:
			return None
		else:
			return idLab[0]
			
	def addNodes(self, child, connection, _type, prompt, labId, _oslBin):
	
		nodesDict = {}
		
		nodeList = self.runCmd(child, _oslBin + 'extractFlatComplexData ' + _type, prompt)[0].split()

		self.log.debug('nodelist: ' + str(nodeList))
		try:
			for node in nodeList:
				tempHwType = self.runCmd(child, _oslBin + 's_rsh ' + node + ' cat /etc/hw_config',  prompt)
				for line in tempHwType:
					if 'HW_TYPE' in line:
						tempHwType = line.split('"')[1]
						break

				self.log.debug('HW TYPE: ' + str(tempHwType))

				hwType = self.getHwType(tempHwType)
				hwTypeId = self.getHwIdByName(connection, hwType)
				if _type == 'ts':
					self.addTS(connection, labId, hwTypeId, node)
				elif _type == 'ms':
					self.addMS(connection, labId, hwTypeId, node)
				else: 
					raise Exception('addNodes. Unknown type: ' + str(_type))
				nodesDict[node] = hwTypeId
		except TimeoutReached, err:
			raise TimeoutReached(str(err))
		
		return nodesDict
	
	def addMS(self, connection, labId, hwTypeId, ms):
		# Check if given MS already exists
		msId = self.getMsIdByData(connection, labId, hwTypeId, ms)
		if msId == None:
			self.log.info('Adding new MS (' + ms + ')...')
			connection.execute(''' INSERT INTO MS (MS_TYPE_idHW_TYPE, LAB_idLAB, NAME) VALUES (?, ?, ?) ''', (hwTypeId, labId, ms))

	def addTS(self, connection, labId, hwTypeId, ts):
		# Check if given TS already exists
		tsId = self.getTsIdByData(connection, labId, hwTypeId, ts)
		if tsId == None:
			self.log.info('Adding new TS (' + ts + ')...')
			connection.execute(''' INSERT INTO TS (TS_TYPE_idHW_TYPE, LAB_idLAB, NAME) VALUES (?, ?, ?) ''', (hwTypeId, labId, ts))
			
	def addSU(self, child, prompt, connection, labId):
		
		last = ''
		
		''' Get FROM, TO and SU type'''
		staged = self.runCmd(child, 'grep "swupg_download: Staged" /su/log/swupg.acs01.log 2>/dev/null', prompt)
		if not staged:
			self.log.info('No SU data available. Skipping...')
			return False, False
		else:				
			try:
				for line in staged:
					if line.startswith('acs01'):						
						suFrom = line.split()[8]
						suTo = line.split()[6].replace(',', '').strip()
						break
			except Exception, err:
				self.log.debug('Cannot retrieve Su data: ' + str(err))
				return False, False
		suType = self.runCmd(child, 'grep swupg_preinstall /su/log/swupg.acs01.log 2>/dev/null', prompt)
		if suType: 
			suType = 'NZDT'
		else:
			suType = self.runCmd(child, 'grep swupg_install: /su/log/swupg.acs01.log 2>/dev/null', prompt)
			if suType:
				suType = 'nonNZDT'
			else:
				suType = 'SWUPG'	
		#
		# If release levels are different overwrite suType with 'SWUPG'
		#
		if suFrom.split('.')[0] != suTo.split('.')[0]:
			suType = 'SWUPG'			
		
		#
		# Retrieve SU_TYPE ID
		#
		suTypeId = self.getSuIdByName(connection, suType)

		self.log.debug('SU FROM: ' + suFrom + ', SU TO: ' + suTo + ', SU TYPE: ' + suType + ' (ID: ' + str(suTypeId) + ')')
		
		#
		# Retrieve SU_START_TIME (Actually start of download phase on acs01) 
		#
		downloadInProgress = self.runCmd(child, 'grep "download in_progress" /su/log/swupg.acs01.log 2> /dev/null', prompt)
		if downloadInProgress:
			for line in downloadInProgress:
				if line.startswith('acs01'):
					suStartTime = line.split()[1] + ' ' + line.split()[2]
					break
			self.log.debug('SU START TIME: ' + str(suStartTime))
		else:
			self.log.debug('SU was not started. Skipping...')
			return False, False
		
		#
		# Retrieve SU_END_TIME (Actually end of rollback, commit or soak on acs01)
		#
		rollbackCompleted = self.runCmd(child, 'grep "Changing state to rollback completed" /su/log/swupg.acs01.log 2>/dev/null', prompt)
		if rollbackCompleted:
			self.log.info('SU STATE: rollback completed')
			self.log.debug(str(rollbackCompleted))
			suState = 'rollback'
			suEndTime = rollbackCompleted[0].split()[1] + ' ' + rollbackCompleted[0].split()[2]			
		else:
			self.log.debug('SU not rolled back')
			commitCompleted = self.runCmd(child, 'grep "Changing state to commit completed" /su/log/swupg.acs01.log 2>/dev/null', prompt)
			if commitCompleted:
				self.log.debug(str(commitCompleted))
				self.log.info('SU STATE: commit completed')
				suState = 'commit'				
				suEndTime = commitCompleted[0].split()[1] + ' ' + commitCompleted[0].split()[2]
				last = '.last'
			else:
				self.log.info('SU was not commited...')
				underUserTest = self.runCmd(child, 'grep under_user_test /su/log/swupg.acs01.log 2>/dev/null', prompt)
				if underUserTest:
					self.log.debug(str(underUserTest))
					self.log.info('SU STATE: soak')
					suState = 'soak'
					for line in underUserTest:
						if line.startswith('acs01'):
							suEndTime = line.split()[1] + line.split()[2]
							break
				else:
					return False, False
						
		self.log.debug('SU END TIME: ' + str(suEndTime))
		
		suStateId = self.getSuStateIdByName(connection, suState)
		self.log.debug('SU STATE ID: ' + str(suStateId))
		#
		# Check if given SU was not already added
		#
		idSu = self.getSuIdByData(connection, suTypeId, labId, suFrom, suTo, suStartTime, suEndTime, suStateId)
		if idSu == None:
			self.log.info('Adding new SU...')
			connection.execute(''' INSERT INTO SU (SU_TYPE_idSU_TYPE, LAB_idLAB, SU_FROM, SU_TO, SU_START_TIME, SU_END_TIME, SU_STATE_idSU_STATE)
				VALUES (?, ?, ?, ?, ?, ?, ?)''', (suTypeId, labId, suFrom, suTo, suStartTime, suEndTime, suStateId))
			idSu = self.getSuIdByData(connection, suTypeId, labId, suFrom, suTo, suStartTime, suEndTime, suStateId)
		else:
			self.log.info('SU already added.')
			
		self.log.debug('SU ID: ' + str(idSu))
		return idSu, last
	
	def getLogFile(self, child, PROMPT, c, node, last):
		suLog = ''
		if node == 'acs01':		
			rawSuLog = self.runCmd(child, '/bin/ksh -c "grep Executing /su/log/swupg.acs01.log | grep \"^acs01\""', PROMPT)
		elif node == 'acs02':
			rawSuLog = self.runCmd(child, '$OSL_BIN/s_rsh osl02 /bin/ksh -c \"\\\"grep Executing /su/log/swupg.acs02.log | grep \"^acs02\" \\\"\"', PROMPT)
		else:
			rawSuLog = self.runCmd(child, '$OSL_BIN/s_rsh ' + node + ' /bin/ksh -c \"\\\"grep SU /update/su_log' + last + ' 2> /dev/null| grep state | grep changed \\\"\"', PROMPT)
			if not rawSuLog:
				rawSuLog = 'no file'
		for line in rawSuLog:
			suLog += line + '\n'
			
		return suLog
	
	def calculateNoOfErrors(self, _log):
		""" Calculate the number of errors based on SU timeline """
		
		_total = 0
		_current = ''
		_next = ''
		_logOut = ''
		
		for line in _log.splitlines():
			if not _current:
				_current = ''.join(line.split()[4:])
				_logOut += line + '\n'
				continue
			else:
				_next = ''.join(line.split()[4:])
				if _current == _next and \
					_current != 'swupg_rollback:ExecutingtaskremoveSS7RouteRule:removingincorrectroutingrulesaddedbySS7processes...' and \
					_current != 'SUstatechangedtodownloadin_progress' and \
					_current != 'SUstatechangedtopreinstallin_progress' and \
					_current != 'SUstatechangedtoswitchoverin_progress' and \
					_current != 'SUstatechangedtoinstallRedin_progress' and \
					_current != 'SUstatechangedtoinstallBluein_progress' and \
					_current != 'SUstatechangedtocommitin_progress' and \
					_current != 'SUstatechangedtorollbackin_progress':
					self.log.info('Found error: ' + str(_next))			
					_total += 1
					line = '----ERROR----> ' + line
				_current = _next
				_logOut += line + '\n'
		return _total, _logOut
	
	def addLog(self, c, hwId, nodeTypeId, suId, logFile, node):
		_errors = 0
		
		logId = self.getLogIdByData(c, hwId, nodeTypeId, suId, logFile, node)
		if logId == None:
			_errors, logFile = self.calculateNoOfErrors(logFile)
			
			self.log.info('Adding new log for ' + str(node) + '...')
			c.execute(''' INSERT INTO SU_LOG (HW_TYPE_idHW_TYPE, NODE_TYPE_idNODE_TYPE,
						SU_idSU, LOG_FILE, NODE_NAME, LOG_ERRORS) 
						VALUES (?, ?, ?, ?, ?, ?)''', (hwId, nodeTypeId, suId, logFile, node, _errors))
			logId = self.getLogIdByData(c, hwId, nodeTypeId, suId, logFile, node)
			self.log.info('SU LOG ID: ' + str(logId))
		else:
			self.log.info('SU LOG already added')
			
		self.log.info('SU ERRORS: ' + str(_errors))
		
		return _errors						
			
	def addSuLogs(self, child, PROMPT, c, suId, acsHwId, msNodesD, tsNodesD, last):
		
		_totalErrors = 0
		
		acsNodeTypeId = self.getNodeTypeIdByName(c, 'acs')		
		# acs01 log		
		self.log.info('Processing acs01...')
		logFile = self.getLogFile(child, PROMPT, c, 'acs01', last='')
		_totalErrors += self.addLog(c, acsHwId, acsNodeTypeId, suId, logFile, 'acs01')	
		
		# acs02 log
		self.log.info('Processing acs02...')
		logFile = self.getLogFile(child, PROMPT, c, 'acs02', last='')
		_totalErrors += self.addLog(c, acsHwId, acsNodeTypeId, suId, logFile, 'acs02')	

		# ms logs
		msNodeTypeId = self.getNodeTypeIdByName(c, 'ms')
		
		for ms in msNodesD.keys():
			self.log.info('Processing ' + str(ms) + '...')
			logFile = self.getLogFile(child, PROMPT, c, ms, last)
			_totalErrors += self.addLog(c, msNodesD[ms], msNodeTypeId, suId, logFile, ms)
			
		# ts logs
		tsNodeTypeId = self.getNodeTypeIdByName(c, 'ts')
		
		for ts in tsNodesD.keys():
			self.log.info('Processing ' + str(ts) + '...')
			logFile = self.getLogFile(child, PROMPT, c, ts, last)
			_totalErrors += self.addLog(c, tsNodesD[ts], tsNodeTypeId, suId, logFile, ts)	
			
		return _totalErrors	

	def updateSUwithErrors(self, _suId, _totalErrors, _c):
		""" Update SU with the total number of errors """
		self.log.info('Update SU: ' + str(_suId) + ' with total number of errors: ' + str(_totalErrors))
		
		_c.execute(''' UPDATE SU SET SU_ERRORS = ? WHERE idSU = ? ''', (_totalErrors, _suId))
		
		
	def run(self):
			
		self.log.info('----------============ Starting ...')
		PROMPT = '(SunOS#|Linux#)*root@acs01.' + self.lab + '# '

		try:
			child = pexpect.spawn('lab ' + self.lab)
			rc = child.expect(['swupg_state: No such file or directory(.*)' + PROMPT, 'swupg_state(.*)' + PROMPT, pexpect.TIMEOUT, pexpect.EOF])

			if rc == 2 or rc == 3:				
				raise TimeoutReached('Cannot login to the lab ' + str(self.lab) + '. Skipping...')
		except TimeoutReached, err:
			self.log.info(str(err))
			return
			
		OS = self.runCmd(child, 'uname -s', PROMPT)[0]
		if OS == 'SunOS':
			DB_CONFIG = '/db/config/'
			ipType = self.runCmd(child, '/bin/ksh -c "$OSL_BIN/extractFlatComplexData ipgw | grep ipgw > /dev/null 2>&1 && echo \"IPGW\" || echo \"nonIPGW\""', PROMPT)[0]
			OSL_BIN = '/opt/lucent/anypath/osl/bin/'
			MBL_ETC = '/opt/lucent/anypath/mbl/etc/'
		else:
			DB_CONFIG = '/apdata/acs/config/'
			ipType = 'IPGW'
			OSL_BIN = '/apsw/acs/osl/bin/'
			MBL_ETC = '/apsw/acs/mbl/etc/'

		try:
			# NAME
			name = self.runCmd(child, 'grep COMPLEX ' + DB_CONFIG + 'acs01.acsConfig', PROMPT)[0].split('=')[1]

			# NO_OF_LANGS 
			noOfLangs = len(self.runCmd(child, OSL_BIN + 'admLanguages -L', PROMPT)) - 5
			
			# HAP
			hap = self.runCmd(child, 'grep HAP ' + MBL_ETC + 'sdapdHAP.rc', PROMPT)[0].split('=')[1]

			# RMS
			rms = self.runCmd(child, OSL_BIN + 'verifyFeatStat -f RMS', PROMPT)
			if 'Redundant Message Server feature is enabled' in rms:
				rms = 'ON'
			else:
				rms = 'OFF'
			
			# DUALIP
			dualIp = self.runCmd(child, 'grep CTRAF01IP ' + DB_CONFIG + 'acs01.acsConfig', PROMPT)
			if dualIp:
				dualIp = 'ON'
			else:
				dualIp = 'OFF'

			# HW_TYPE
			unameOut = self.runCmd(child, 'uname -i', PROMPT)[0]
			acsHwType = self.getHwType(unameOut)

			self.log.info('NAME: ' + str(name) + ', NO_OF_LANGS: ' + str(noOfLangs) + ', HAP: ' + str(hap) + ', RMS: ' + str(rms) + ', DUAL IP: ' + str(dualIp) + ', ACS_TYPE: ' + str(acsHwType) + ', IP TYPE: ' + str(ipType))

		except Exception, err:
			self.log.info(str(err))
			self.log.debug('Skipping')
			return 
			
		try:
			conn = connect(DB)
			c = conn.cursor()

			# Retrieve HW TYPE for ACS
			acsHwId = self.getHwIdByName(c, acsHwType) 

			# Retrieve IP TYPE for given LAB
			ipTypeId = self.getIpIdByName(c, ipType)

			# Add a lab if not exists and return its labid
			labId = self.addLab(c, name, noOfLangs, hap, rms, dualIp, acsHwId, ipTypeId) 

			# Add ms and ts nodes
			msNodesD = self.addNodes(child, c, 'ms', PROMPT, labId, OSL_BIN)
			tsNodesD = self.addNodes(child, c, 'ts', PROMPT, labId, OSL_BIN)			
		
			if msNodesD and tsNodesD:
				# Add SU
				suId, last = self.addSU(child, PROMPT, c, labId)
				
				if suId:			
					# Add SU logs
					totalErrors = self.addSuLogs(child, PROMPT, c, suId, acsHwId, msNodesD, tsNodesD, last)
					
					# Update SU with the total number of failures
					self.updateSUwithErrors(suId, totalErrors, c)
		
			conn.commit()
		except TimeoutReached, err:
			self.log.debug(str(err))
			self.log.debug('Skipping')
			conn.commit()
			conn.close()
			return 
		except Exception, err:
			self.log.debug('ERROR: ' + str(err))
			sys.exit(1)
		finally:
			conn.close()

class SuDetectiveRunner():
	def __init__(self):
		pass
	
	def getLabs(self, _labFile):
		
		labs = []		
		with open(_labFile) as f:
			data = f.readlines()
			#
			#name:acs01 address:acs02 address:vip address:tsc pass:root pass:ssh
			#
			for line in data:
				labs.append(line.split(':')[0].lower())
			
		return labs
	
	def initSuDetectiveThreads(self):
		labs = self.getLabs(LAB_FILE)
		#labs = ['robo']
		#labs = ['willow']
		
		startedThreads = dict()
		
		try:
			while labs:
				logging.debug('List of detected labs: ' + str(labs))
				for i in range(MAX_THREADS):
					if len(startedThreads) < MAX_THREADS:
						try:
							logger = MyLog(labs[i])	
							suThread = SUDetective(labs[i], logger)
							suThread.start()
							startedThreads[labs[i]] = suThread
							time.sleep(3)
						except IndexError, err:
							pass
					
				''' Wait for running threads and remove them from the list and from dictionary '''
				for lab in startedThreads.keys():
					startedThreads[lab].join()
					labs.remove(lab)
					startedThreads.pop(lab)
		except Exception, err:
			logging.debug('initSuDetectiveThreads exception: ' + str(err))
			return				
				
				
def main():
	logging.info('----------============ START ' + NAME + ' VERSION: ' + VERSION + ' ============----------')
	sd = SuDetectiveRunner()
	sd.initSuDetectiveThreads()
	logging.info('----------============ END ============----------')

if __name__ == '__main__':
	main()
