class A:
    __slots__ = ['michal']

a = A()
a.michal = 1

print(f'Slots class attrs has __slots__: {dir(a)}')

class B:
    pass
b = B()

print(f'Regualar class attrs has __dict__ and __weakref__: {dir(a)}')

