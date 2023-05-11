class A():
    def p(self):
        return 3
class B():
    def p(self):
        return 5
class C(B, A):
    def c(self):
        return 6

c = C()
print(c.p())
