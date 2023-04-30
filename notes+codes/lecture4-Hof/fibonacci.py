def fib(n):
    """compute the nth Fibonacci number for n >= 0
    >>> a = fib(0)
    >>> a
    0
    >>> b = fib(1)
    >>> b
    1
    >>> c = fib(2)
    >>> c
    1
    >>> d, e = fib(3), fib(4)
    >>> d, e
    (2, 3)


    """
    twobehind = 1
    onebehind = 0
    fib = 0
    i = 0
    while i < n:
        fib = onebehind + twobehind
        tmp = onebehind
        onebehind = fib
        twobehind = tmp
        i += 1
    return fib
