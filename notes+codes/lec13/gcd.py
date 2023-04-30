def gcd(m, n):
    lim = min(m, n)
    i = 2
    ans = 1
    while i <= lim:
        if m % i == 0 and n % i == 0:
            ans = i
        i += 1
    return ans
print(gcd(27, 9))
