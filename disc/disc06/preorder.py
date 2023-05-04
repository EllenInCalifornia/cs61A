from tree import *
def preorder(t):

    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).
    mid- left - right

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    cur = []

    def helper(t, cur):
        cur.append(label(t))
        for b in branches(t):
            helper(b, cur)

    helper(t, cur)
    return cur

