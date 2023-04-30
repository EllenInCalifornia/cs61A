def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)
grow = lambda n: f_then_g(grow, print, n)
shrink = lambda n: f_then_g(shrink, print, n)

# def shrink(n):
#     if n:
#         print(n)
#         shrink_def(n // 10)

# def grow(n):
#     if n:
#         grow(n // 10)
#         print(n)

