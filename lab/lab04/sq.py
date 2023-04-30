def sq(n):
    print(n)
    if n <= 1:
        return n
    else:
        return (sq(n - 1)  + sq(n - 2)) ** 2
sq(3)