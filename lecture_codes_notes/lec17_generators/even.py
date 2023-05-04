def evens(start, end):
    """return iterators that go over even numbers only
     """
    even = start + start % 2
    while even < end:
        yield even
        even += 2