def multiple(m, n):
    if n == 0:
        return 0
    return multiple(m, n - 1) + m
print(multiple(5, 0))