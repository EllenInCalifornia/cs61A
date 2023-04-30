def count_stair_ways(n):
    if n < 2:
        return 1
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)
print(count_stair_ways(2))
def count_stair_ways_alt(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways_alt(4)
    5
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    return count_stair_ways_alt(n-1) + count_stair_ways_alt(n-2)
print(count_stair_ways_alt(10))
