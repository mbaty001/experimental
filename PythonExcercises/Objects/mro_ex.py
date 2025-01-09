class D(object):
    pass
class E(object):
    pass
class F(object):
    pass
class B(D, E):
    pass
class C(E, F):
    pass
class A(B, C):
    pass

print(A.__mro__)
print(A.mro())
