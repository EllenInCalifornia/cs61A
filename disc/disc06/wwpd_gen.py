def infinite_generator(n):
    yield n
    while True:
        n += 1
        yield n

def add_prefix(s, pre):
    if not pre:
        return
    yield pre[0] + s
    yield from add_prefix(s, pre[1:])
    