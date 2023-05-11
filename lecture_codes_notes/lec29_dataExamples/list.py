# append
s = [2, 3]
t = [5, 6]
s.append(t)
t = 0

# extend


# slice assignment
s = [2, 3]
t = [5, [6]]
s[0:0] = t
print(s)
print(t[1:])

# indices of smallest absolute value
l = [-4, -3, -2, 3, 2, 4]
a = min(l, key=abs)
n = map(abs, l)
print(list(n))