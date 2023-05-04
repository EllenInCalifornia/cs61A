# generator function
"""there are many possibilities,
 and you only want a few of them"""
def partition_y(n, m):
    if n > 0 and m> 0:
        if n == m:
            yield str(m)
        for p in partition_y(n-m, m):
            yield p + ' + ' + str(m)
        yield from partition_y(n, m-1)