class A(object):

    def __init__(self, a):
        self.__a = a

    def geta(self):
        return self.__a

a = A(1)
print(a._A__a)
print(a.geta())

class B(A):
    pass

b = B(2)
print(dir(b))
print(b.geta())