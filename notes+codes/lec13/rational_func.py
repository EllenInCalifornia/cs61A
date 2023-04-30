def rational(n, d):
    def select(name):
        if name == "numer":
            return n
        elif name == "denom":
            return d
    return select

x = rational(1, 3)

def numer(x):
    return x("numer")
print(numer(x))