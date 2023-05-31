from operator import mul, truediv


def reduce(f, s, initial):
    """Combine elements of a pairwise using f, starting with initial.
   E.g., reduce(mul, [2, 4, 8], 1) is equivalent to mul(mul(mul(1, 2), 4), 8)
   >>> reduce(mul, [2, 4, 8], 1)
   64
    """
    def helper(s, initial):
        if not s:
            return initial
        initial = f(s[0], initial)
        return helper(s[1:], initial)
    return helper(s, initial)


# 老师的解法：
def reduce_official(f, s, initial):
    for x in s:
        initial = f(initial, x)
    return initial

def reduce_recur(f, s, initial):
    if not s:
        return initial
    else:
        first, rest = s[0], s[1:]
        return reduce_recur(f, rest, f(initial, first))
a = reduce(mul, [1, 2, 4, 5], 1)
print(a)

def divide_all(n, ds):
    try:
        return reduce_recur(truediv, ds, n)
    except ZeroDivisionError:
        return float('inf')