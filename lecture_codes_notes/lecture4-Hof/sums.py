def identity(k):
    return k
def cube(k):
    return pow(k, 3)
def pi_term(k):
    return 8 / ((4 * k - 3) * (4 * k - 1))
def summation(n, term):
    """
    >>> summation(5, identity)
    15
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total



'''before generalization'''
def sum_naturals(n):
    """"return 1 + 2 +.. + n
    >>> sum_naturals(5)
    15
    """
    # k is the next number to add
    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def sum_cubes(n):
    """return the sume of first n cubes of natural numbers
    >>> sum_cubes(5)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1
    return total