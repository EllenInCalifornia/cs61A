# built_in any()
def digit_dict(s):
    """map each digit d to the lists of elements in s that end with d
    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    return {d:[x for x in s if x % 10 == d] for d in range(10) if any([i % 10 == d for i in s])}

# breakup
def digit_dict(s):
    last_digit = [x % 10 for x in s]
    return {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digit}