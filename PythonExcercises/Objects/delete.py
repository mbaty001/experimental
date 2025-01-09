class A():
    def __del__(self):
        print("i po kechuku")

a = A()

del a