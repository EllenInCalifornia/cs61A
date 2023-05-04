def remove(n, digit):
    """return all digits of non-negative N that are not DIGIT,
    for some non-negative DIGIT less than 10
   >>> remove(231, 3)
   21
   >>> remove(243132, 2)
   4313
    """
    # kept： 记录是第几位 10 ** kept
    kept, digits = 0, 0
    while n != 0:
        n, last = n // 10, n % 10
        if last != digit:
            digits += last * 10 ** kept
            kept += 1
    return digits