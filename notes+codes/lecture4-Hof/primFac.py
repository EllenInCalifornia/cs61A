def prime_factors(n):
    """print the prime factors of n in increasing order
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5

    """
    while n != 1:
        factor = smallest_prime_factor(n)
        print(factor)
        n //= factor

def smallest_prime_factor(n):
    """
    >>> a = smallest_prime_factor(6)
    >>> a
    2
    >>> b = smallest_prime_factor(9)
    >>> b
    3
    >>> c = smallest_prime_factor(7)
    >>> c
    7

    """
    k = 2
    while n % k != 0:
        k += 1
    return k
