def search(f):
    """search a positive integer such that f(x) == True"""
    x = 0
    while True:
        if f(x):
            return x
        x += 1
def square(x):
    return x * x

def inverse(f):
    """return a function g such that g((f(x)) = x"""
    return lambda y: search(lambda x: f(x) == y)
