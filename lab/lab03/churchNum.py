 # apply f zero time
def zero(f):
     return lambda x: x

# apply f once
def one(f):
    return lambda x: f(x)

def two(f):
    return lambda x: f(f(x))

def successor(n):
   return lambda f: lambda x: f(n(f)(x))

def church_to_int(n):
    return n(lambda x: x + 1)(0)

def add_church(m, n):
     return lambda f: lambda x: m(f)(n(f)(x))

def mul_church(m, n):
     return lambda f: m(n(f))

def pow_church(m, n): # m ** n
    return n(m)
