from link import *
def convert_link(link):

    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    res = []
    while link is not Link.empty:
        res.append(link.first)
        link = link.rest
    return res


def convert_link_recr(link):

    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    if Link.empty:
        return []
    rest = convert_link(link.rest)
    rest.insert(0, link.first)
    return rest