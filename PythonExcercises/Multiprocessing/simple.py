import multiprocessing
import time


#http://eli.thegreenplace.net/2012/01/16/python-parallelizing-cpu-bound-tasks-with-multiprocessing

def worker(the_string, the_file):
	try:
		with open(the_file, 'r') as fyle:
			buf = fyle.read()
			if the_string in buf:
				#print '%s FOUND in %s' %(the_string, the_file)
				pass
			else:
				#print '%s NOT FOUND in %s' %(the_string, the_file)
				pass
	except Exception, err:
		print str(err)
		return 1
	
if __name__ == '__main__':

	start_time = time.time()
	
	plist = list()
	for number in xrange(100):
		p = multiprocessing.Process(target=worker, args=('ala', '/home/test/research/glassfish3/jdk7/jre/lib/rt.jar'))
		p.start()
		plist.append(p)
		p.join()
	
	
	print 'time: %s' %(time.time() - start_time)
	
	start_time = time.time()

	for number in xrange(100):	
		worker('ala', '/home/test/research/glassfish3/jdk7/jre/lib/rt.jar')
	
	print 'time: %s' %(time.time() - start_time)