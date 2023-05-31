def evenSub(s):
    if not s:
        return []
    if len(s) == 1:
        if s[0] % 2 == 0:
            return [[s[0]]]
        else:
            return []
    else:
        notFirst = evenSub(s[1:])

        if s[0] % 2 == 0:
            withFirst = [[s[0]]] + [[s[0]] + sub for sub in notFirst]
        else:
            withFirst = [[s[0]] + sub for sub in oddSub(s[1:])]
        return notFirst + withFirst

def oddSub(s):
    if not s:
        return []
    if len(s) == 1:
        if s[0] % 2 != 0:
            return [[s[0]]]
        else:
            return []
    else:
        notFirst = oddSub(s[1:])
        if s[0] % 2 == 0:
            withFirst = [[s[0]] + sub for sub in notFirst]
        else:
            withFirst = [[s[0]]] + [[s[0]] + sub for sub in evenSub(s[1:])]
        return notFirst + withFirst
s = [1, 2, 3, 4, 5, 6, 7]
a = [[7], [6, 7], [5], [5, 6], [4, 7], [4, 6, 7], [4, 5], [4, 5, 6], [3], [3, 6], [3, 5, 7], [3, 5, 6, 7], [3, 4], [3, 4, 6], [3, 4, 5, 7], [3, 4, 5, 6, 7], [2, 7], [2, 6, 7], [2, 5], [2, 5, 6], [2, 4, 7], [2, 4, 6, 7], [2, 4, 5], [2, 4, 5, 6], [2, 3], [2, 3, 6], [2, 3, 5, 7], [2, 3, 5, 6, 7], [2, 3, 4], [2, 3, 4, 6], [2, 3, 4, 5, 7], [2, 3, 4, 5, 6, 7], [1], [1, 6], [1, 5, 7], [1, 5, 6, 7], [1, 4], [1, 4, 6], [1, 4, 5, 7], [1, 4, 5, 6, 7], [1, 3, 7], [1, 3, 6, 7], [1, 3, 5], [1, 3, 5, 6], [1, 3, 4, 7], [1, 3, 4, 6, 7], [1, 3, 4, 5], [1, 3, 4, 5, 6], [1, 2], [1, 2, 6], [1, 2, 5, 7], [1, 2, 5, 6, 7], [1, 2, 4], [1, 2, 4, 6], [1, 2, 4, 5, 7], [1, 2, 4, 5, 6, 7], [1, 2, 3, 7], [1, 2, 3, 6, 7], [1, 2, 3, 5], [1, 2, 3, 5, 6], [1, 2, 3, 4, 7], [1, 2, 3, 4, 6, 7], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6]]
b = filter(lambda lst: sum(lst) % 2 == 0, a)
print(list(b))