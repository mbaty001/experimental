class Ten:
    def __get__(self, obj, objtype=None):
        return 10
    
class A:
    x = 5
    y = Ten() # descriptor instance

a = A()

print(a.y())

print(f"__dict__ attributes: {a.__dict__}")
