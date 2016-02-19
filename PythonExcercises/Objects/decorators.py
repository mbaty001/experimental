'''
Created on Jan 14, 2016

@author: test
'''

class Function_wrapper(object):

    def __init__(self, func):
        self.func = func

    def __call__(self):
        print "Entering", self.func.__name__
        self.func()
        print "Exited", self.func.__name__

@Function_wrapper
def funct():
	print 'kuku'
	
''' without decorator Function_wrapper(funct)()'''
	
funct()

''' second example '''

def func_wrapper(f):
    def new_f():
        print "Entering", f.__name__
        f()
        print "Exited", f.__name__
    return new_f
   
@func_wrapper
def functi():
	print 'kuku'
	
functi()