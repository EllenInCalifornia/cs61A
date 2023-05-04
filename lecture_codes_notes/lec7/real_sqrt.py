"""evaluation rule for conditional statements VS for call expressions """
from math import sqrt

def real_sqrt_cs(x):
    if x > 0:
        return sqrt(x)
    else:
        return 0
def if_(c, t, f):
    if c:
        return t
    else:
        return f
def real_sqrt_ce(x):
    return if_(x > 0, sqrt(x), 0) # error when arguments is evaluated