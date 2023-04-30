def count_k(n, k):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    ans = 0
    i = 1
    while i <= k:
        ans += count_k(n - i, k)
        i += 1
    return ans

def count_k2(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        total = 0
        i = 1
        while i <= k:
            total += count_k(n - i, k)
            i += 1

        return total
print(count_k(10, 4))
print(count_k2(10, 4))
