'''
Created on Jan 14, 2016

@author: test
'''

class A(object):
	
	VALUE = 0

	def __init__(self, value):
		self.value = value
	
	def local(self):
		print self.value
		
	@staticmethod
	def local_static():
		print A.VALUE
		
	@classmethod
	def local_class(cls):
		print cls.VALUE

class B(A):
	VALUE= 5
			
a = A('10')
b = B('7')

a.local() # 10 
A.local_static() # 0
A.local_class() #0

b.local() # 7
B.local_static() #0
B.local_class() #5
