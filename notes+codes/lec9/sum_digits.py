def split(n):
    return n // 10, n % 10


def sum_digts(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digts(all_but_last) + last