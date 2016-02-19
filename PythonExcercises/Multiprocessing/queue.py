'''
Created on Jan 15, 2016

@author: test
'''

import multiprocessing
import random

def writer(queue):
	
	while True:
		value = random.randrange(10)
		queue.put(value)
		print 'value added to queue: %s' %value
	
def reader(queue):
	while True:
		value = queue.get()
		print 'value read from queue: %s' %value

if __name__ == '__main__':
	
	queue = multiprocessing.Queue()
	
	p1 = multiprocessing.Process(target=writer, args=(queue,))
	
	p2 = multiprocessing.Process(target=reader, args=(queue,))
	
	p1.start()
	p2.start()