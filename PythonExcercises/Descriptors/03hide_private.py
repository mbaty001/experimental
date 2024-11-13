class Private:

    def __get__(self, obj, objtype=None):
        value = obj._age
        return value

    def __set__(self, obj, value):
        obj._age = value

class Person:

    age = Private()             # Descriptor instance

    def __init__(self, name, age):
        self.name = name                # Regular instance attribute
        self.age = age                  # Calls __set__()
