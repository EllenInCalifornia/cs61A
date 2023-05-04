def counting_partition2(n, m):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if m == 0:
        return 0
    # include m
    with_m = counting_partition2(n - m, m)
    # not include m
    without_m = counting_partition2(n, m - 1)
    return with_m + without_m



