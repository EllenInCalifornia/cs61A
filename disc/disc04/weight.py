def even_weighted_loop(s):
    new_list = []
    for i in range(len(s)):
        if i % 2 == 0:
            new_list.append(s[i] * i)
    return new_list
x = [1, 2, 3, 4, 5, 6]
y = even_weighted_loop(x)

def even_weighted_list_compr(s):
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]
y= even_weighted_list_compr(x)

print(y)
print(a[0])