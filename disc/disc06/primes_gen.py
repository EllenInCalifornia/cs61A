def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    for i in range(n, 1, -1):
        if is_prime(i):
            yield i
def primes_gen2(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen2(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if is_prime(n):
        yield n
    yield from primes_gen(n-1)