def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)


# another definition of exponentiation
""""if n is even, n/2 ** 2"""
def exp_improved(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        # 注意用floor divison
        return exp_improved(b, n // 2) * exp_improved(b, n//2)
    else:
        return b * exp_improved(b, n - 1)

def square(x):
    return x * x

def exp_improved2(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        # 注意用floor divison
        return square(exp_improved(b, n // 2))

    else:
        return b * exp_improved(b, n - 1)
# this is not a tree recursive function, but linear recursion, sometimes reduced by half