from copy import deepcopy

class A(object):
    a = 0

a = A()

a_list = [0,1,a]

a_copy = deepcopy(a_list)

print(a_copy)