def invert(x):
    result = 1 / x
    print("Never printed if x is 0")
    return result

def invert_safe(x):
    try:
        return invert(x)
    except ZeroDivisionError as e:
        return 0

a = invert_safe(0)

