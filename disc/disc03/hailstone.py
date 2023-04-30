def hailstone_rec(n):
    print(n)
    if n == 1:
        return
    if n % 2 == 0:
        hailstone_rec(n // 2)
    else:
        hailstone_rec(n * 3 + 1)
hailstone_rec(10)