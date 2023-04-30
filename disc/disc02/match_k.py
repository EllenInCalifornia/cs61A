def match_k(k):
    """ Return a function that checks if digits k apart match
    this means that from right to left, every k digits repeat a cycle
    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def k_cycle(x):
        cycle_unit = x % 10 ** k # 先算**
        while x > 0:
            if cycle_unit != x % 10 ** k:
                return False
            x //= 10 ** k
        return True
    return k_cycle