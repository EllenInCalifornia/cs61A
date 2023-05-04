from tree import *
def print_sums(t):
    """take in a tree, find all the leaves, for each leaf prints out 
     the sum of all the labels from the root to that leaf"""
    res = []
    cur = 0

    def helper(t, cur):
        cur += label(t)
        if is_leaf(t):
            res.append(cur)
        else:
            for b in branches(t):
                helper(b, cur)
    helper(t, cur)
    for i in res:
        print(i)
t1 = fib_tree(4)
t2 = fib_tree(2)

print(t1, t2)
print_sums(t1)


"""老师的approach"""
def print_sums_official(t, so_far):
    so_far += label(t)
    if is_leaf(t):
        print(so_far)
    else:
        for b in branches(t):
            print_sums(b)

