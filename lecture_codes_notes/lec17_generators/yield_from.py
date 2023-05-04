def a_then_b(a, b):
    for x in a:
        yield x
    for x in b:
        yield x
#  等价于

def a_then_b2(a, b):
    yield from a
    yield from b

def countdown(k):
    if k > 0:
        yield k
        yield from countdown(k-1)
# 等价
def countdown2(k):
    if k > 0:
        yield k
        for x in countdown(k-1):
            yield x
def prefixes(s):
    if s:
        for x in prefixes(s[:-1]):
            yield x
        yield s
# 等价于
def prefixes2(s):
    if s:
        yield from prefixes(s[:-1])
        yield s

def substrings(s):
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])
