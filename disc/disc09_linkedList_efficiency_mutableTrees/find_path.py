import sys
sys.path.append('/Users/XL/Desktop/a61/disc')
from disc.disc06.tree import *
def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """

    paths = []
    if label(tree) == entry:
        paths = [[label(tree)]]
    for b in branches(tree):
        for p in find_paths(b, entry):
            path = [label(tree)] + p
            paths.append(path)
    return paths
"""答案，基本一致
paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        for path in find_paths(b, entry):
            paths.append([t.label] + path)
    return paths
    """



