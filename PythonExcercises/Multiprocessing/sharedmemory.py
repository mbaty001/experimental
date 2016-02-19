'''
Created on Jan 15, 2016

@author: test
'''
import multiprocessing
import random

def worker(num, arr):
	while True:
		num.value = random.randrange(10)
		for i in range(len(arr)):
			arr[i] = random.randrange(5)

def reader(num, arr):
	while True:
		print 'NUM: %s' %num.value
		print 'ARR: %s' %arr[:]
		
if __name__ == '__main__':
	num = multiprocessing.Value('d', 0.0)
	arr = multiprocessing.Array('i', range(10))
	
	multiprocessing.Process(target=worker, args=(num, arr)).start()
	
	multiprocessing.Process(target=reader, args=(num, arr)).start()
	