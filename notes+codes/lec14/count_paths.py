from tree import *
"""return the number of paths from the root to any node in tree t for 
which the labels along the path sum to total"""
def count_paths(t, total):
    so_far = 0
    ans = 0
    def helper(t, so_far):
        nonlocal ans
        so_far += label(t)
        if so_far == total:
            ans = ans + 1
        else:
            for b in branches(t):
                helper(b, so_far)
    helper(t, so_far)
    return ans
t = fib_tree(3)
paths = count_paths(t, 3)

"""老师的approach"""

def count_paths_official(t, total):
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum([count_paths_official(b, total - label(t)) for b in branches(t)])





