def isPrime(n):
    assert n > 1, "illegal argument"
    def helper(i): # 2 <= i <= n
        if i == n:
            return True
        if n % i == 0:
            return False
        else:
            return helper(i + 1)
    return helper(2)


