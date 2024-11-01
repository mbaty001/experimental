class A(object):
    def __init__(self) -> None:
        print (f"Init from class: A")

class B(A):
    def __init__(self) -> None:
        print (f"Init from class: B")
        super().__init__()

class C(A):
    def __init__(self) -> None:
        print (f"Init from class: C")
        super().__init__()

class D(B, C):
    def __init__(self) -> None:
        print (f"Init from class: D")
        super().__init__()

d = D()



