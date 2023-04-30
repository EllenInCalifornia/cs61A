def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch)
    # return [label, branches] # [lable] + list(branches)
    return [label] + list(branches) # [lable] + list(branches)

def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:] # tree[1:]
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True
def is_leaf(tree):
    return not branches(tree)
def fib_tree(n):
    # base case 0, 1 are leaf, from 2 there is a structure
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
    return tree(label(left) + label(right), [left, right])
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(tree)])
def leaves(tree):
    """"return a list constaining the leaf labels of tree"""
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

""""creating trees"""
def increment_leaves(t):
    """return a tree like t but
    with leaf labels incremented"""
    if is_leaf(t):
        return tree(label(t) + 1)
    bs = [increment_leaves(b) for b in branches(t)]
    return tree(label(t), bs)
def increment(t):
    """" return a tree like t but with all labels incremented
    自己的答案
    """
    if is_leaf(t):
        return tree(label(t) + 1)
    bs = [increment(b) for b in branches(tree)]
    return tree(label(t) + 1, bs)
# 老师的答案- increment
def increment_official(t):
    return [label(t) + 1, [increment_official(b) for b in branches(t)]]

# list comprehension, if the list is empty, it returns an empty list
e = []
f = [x + 1 for x in e]

a = sum([[1,2]], [])

def print_tree(t, indent = 0):
    print("  " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)
fb = fib_tree(2)



"""summing all the labels along a path from the root to the leaf of 
 a tree, and then print out the sum"""