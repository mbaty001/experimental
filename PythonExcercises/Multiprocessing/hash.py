'''
Created on Jan 15, 2016

@author: test
'''

import hashlib
import os
import sys
import time
import multiprocessing
from docutils.parsers.rst.directives.parts import Contents
from pip._vendor.distlib.locators import HASHER_HASH

def hashfile(file_name):
	try:
		with open(file_name, 'rb') as fyle:
			contents = fyle.read()
			
		hasher = hashlib.sha256()
		hasher.update(contents)
		print '%s, %s' %(file_name, hasher.hexdigest())
		del hasher
		return 0
	except Exception, err:
		sys.exit(1)		

if __name__ == '__main__':
	
	start = time.time()
	core1 = multiprocessing.Process(target=hashfile, args=('/media/sf_C_DRIVE/Praca/debian-8.2.0-amd64-netinst.iso',))
	core1.start()	
	
	core2 = multiprocessing.Process(target=hashfile, args=('/media/sf_C_DRIVE/Praca/debian-8.2.0-amd64-netinst.iso',))
	core2.start()
	core1.join()
	core2.join()
	
	print 'time: %s' %(time.time() - start)
	
	start = time.time()
	corePool = multiprocessing.Pool(processes=2)
	
	results = corePool.map(hashfile, ('/media/sf_C_DRIVE/Praca/debian-8.2.0-amd64-netinst.iso', '/media/sf_C_DRIVE/Praca/debian-8.2.0-amd64-netinst.iso'))
	print results
	print 'time: %s' %(time.time() - start)