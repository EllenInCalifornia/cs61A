a = range(3, 7)
def double(x):
    print("x =", x)
    return x * 2
m = map(double, a)
f = filter(lambda x: x >= 10, m)
# map, filter returns an iterator, which computes results lazily
