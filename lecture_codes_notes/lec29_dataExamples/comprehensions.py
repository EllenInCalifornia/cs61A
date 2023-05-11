def min_abs_indices(s):
    """indices of all elements in a list s that have the smallest absolute value
    >>> min_abs_indices([-4, -3, -2,  3,  2,  4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(map(abs, s))

    return [i for i in range(len(s)) if abs(s[i]) == min_abs]

# use map and filter
def min_abs_indices_filter(s):
    """indices of all elements in a list s that have the smallest absolute value
    >>> min_abs_indices([-4, -3, -2,  3,  2,  4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    f = lambda i: abs(s[i]) == min(map(abs, s))
    return list(filter(f, s))

