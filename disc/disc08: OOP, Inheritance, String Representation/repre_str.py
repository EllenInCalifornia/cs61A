"""
1. the print() function calls the __str__ method of the object
and displays the returned string with the quotations removed,
while simply calling the object in interactive mode in the
interpreter calls the _repr__ method
and displays the returned string with the quotations removed.
2. When we define a class in Python, __str__ and __repr__ are
both built-in methods for the class.
3. We can call those methods using the global built-in functions str(obj)
or repr(obj) instead of dot notation, obj.__repr__() or obj.__str__().
4.
"""
class A:
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return self.x

    def __str__(self):
        return self.x * 2

class B:
    def __init__(self):
        print('boo!')
        self.a = []

    def add_a(self, a):
        self.a.append(a)

    def __repr__(self):
        print(len(self.a))
        ret = ''
        for a in self.a:
            ret += str(a)
        return ret