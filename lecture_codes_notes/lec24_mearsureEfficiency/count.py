

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    # counted.call_count is an attribute of the counted function object
    return counted

@count
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

fib = count(fib) # fib 指向counted， 所以每次原fib return 的是count
# count(f) 中的f 指向的是原fib

fib(5) # 每次counted return 的f 指向的是原fib

# 也可以在fib 上加decorator @count

