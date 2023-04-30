def max_product(s):
    ans = 1
    if not s:
        return 1
    if len(s) == 1:
        return s[0]
    if len(s) == 2:
        return max(s[0], s[1])
    if len(s) == 3:
        return max(s[0] * s[2], s[1])

    opt1 = max_product(s[2:]) * s[0]
    opt2 = max_product(s[3:]) * s[1]
    return max(opt1, opt2)

# 答案

def max_pro(s):
    if not s:
        return 1
    return max(s[0] * max_pro(s[2:]), max_pro(s[1:]))
