from tree import *
def sum_tree(t):
    """
    Add all elements in a tree.
    >>> t = tree(4, [tree(2, [tree(3)]), tree(6)])
    >>> sum_tree(t)
    15
    """
    return label(t) if is_leaf(t) else sum([sum_tree(b) for b in branches(t)], label(t))
    # 如果是leaf， sum（）里的list comprehension就不会有了，
    # return label(t) + sum([sum_tree(b) for b in branches(t)])
def balanced(t):
    """
    Checks if each branch has same sum of all elements and
    if each branch is balanced.
    >>> t = tree(1, [tree(3), tree(1, [tree(2)]), tree(1, [tree(1), tree(1)])])
    >>> balanced(t)
    True
    >>> t = tree(1, [t, tree(1)])
    >>> balanced(t)
    False
    >>> t = tree(1, [tree(4), tree(1, [tree(2), tree(1)]), tree(1, [tree(3)])])
    >>> balanced(t)
    False
    """
    return all([sum_tree(branches(t)[0]) == sum_tree(b) and balanced(b) for b in branches(t)])
