class Kuku:

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        print("Get from property")
        return self._x
    
    @x.setter
    def set(self, val):
        print("setter")
        self._x = val


kuku = Kuku(1)
print(kuku.x)
kuku.x = "2"
print(kuku.x)