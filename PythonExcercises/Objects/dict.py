'''
Created on Jan 14, 2016

@author: test
'''

a = ['a', 'b', '1']
a.sort()  # in place - returns None
sorted(a) # does not change a - returns sorted list

d = {'a':'1'}
d.iteritems() #<dictionary-itemiterator object at 0x7fb123706100>
d.items() # [('a', '1')]

''' dictionary sort '''
import operator
import collections
d = {'a' : '1', 'b': '3', 'f':'5', 'z':'2'}
''' 'd.items() -> a list of tuples ('a', '1') ...'''

''' print a sorted list '''
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print sorted_d

''' print a sorted list by keys'''
sorted_d = sorted(d.items())
print sorted_d

''' store sorted in ordered dict '''
orderded_dict_by_key = collections.OrderedDict(sorted(d.items()))
print orderded_dict_by_key

''' store sorted in ordered dict by value'''
orderded_dict_by_value = collections.OrderedDict(sorted(d.items(), key=operator.itemgetter(1)))
print orderded_dict_by_value