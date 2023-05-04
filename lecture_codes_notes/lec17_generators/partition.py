def partition(n, m):
    """"
    >>> partition(6, 4)
   9
    """
    if n == 0:
        return 1
    if m == 0 or n < 0 :
        return 0
    return partition(n - m, m) + partition(n, m-1)

# approach 2
def partition2(n, m):
    if m == 0 or n < 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = partition(n-m, m)
        without_m = partition(n, m - 1)
        return exact_match + with_m + without_m
