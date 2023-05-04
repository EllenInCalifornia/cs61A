def partitions(n, m):
    """partitions(6, 4) returns
    4 + 2
    4 + 1 + 1...
    """
    if n < m:
        return partitions(n, n)
    if m == 0:
        return []
    match = []
    if n == m:
        match = [str(m)]
        return match + partitions(n, m-1)
    with_m = [str(m) + " + " + p for p in partitions(n-m, m)]
    without_m = partitions(n, m-1)
    return with_m + without_m
for p in partitions(6, 4):
    print(p)

