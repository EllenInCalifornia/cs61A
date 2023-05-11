def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

fib = memo(fib)
fib(5)

