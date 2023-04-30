def make_keeper(n):
    def cond(f):
        for i in range(n + 1):
            if f(i):
                print(i)
    return cond
def is_even(x):
    return x % 2 == 0