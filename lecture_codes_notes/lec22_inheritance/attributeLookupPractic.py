class A:
    z = -1

    def f(self, x):
        return B(x-1)

class B(A):
    n = 4

    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    def f(self, x):
        return x

a = A()
b = B(1)
b.n = 5
b.z
b.z.z
C(2)
"""虽然C(2) 用的是B的constructor，但是B里面用的f是C的f"""
b.z.z.z # this is an integer
b.z.z.z.z