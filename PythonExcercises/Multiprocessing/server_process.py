'''
Created on Jan 15, 2016

@author: test
'''

#http://eli.thegreenplace.net/2012/01/24/distributed-computing-in-python-with-multiprocessing

import multiprocessing
import random

def worker(di, li):
	while True: 
		di[0] = random.randrange(10)
		li[0] = random.randrange(4)
	
def reader(di, li):
	while True:
		print 'D: %s' %di
		print 'L: %s' %li
		
if __name__ == '__main__':
	
	manager = multiprocessing.Manager()
	
	di = manager.dict()
	li = manager.list(range(10))
	
	multiprocessing.Process(target=worker, args=(di, li)).start()
	multiprocessing.Process(target=reader, args=(di, li)).start()