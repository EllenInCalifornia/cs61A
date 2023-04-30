def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    return lambda: f1()

def f3():
    """
    >>> f3()(3)
    3
    """
    return lambda x: f1()

def f4():
    """
    >>> f4()()(3)()
    3
    """
    return lambda: lambda x: f1