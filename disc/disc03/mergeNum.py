def merge(n1, n2):

    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    digit1 = n1 % 10
    digit2 = n2 % 10
    if digit1 < digit2:
        return merge(n1 // 10, n2) * 10 + digit1
    else:
        return merge(n1, n2 // 10) * 10 + digit2
print(merge(65, 0))