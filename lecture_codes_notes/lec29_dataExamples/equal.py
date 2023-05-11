def all_have_an_equal(s):
    """Does every element equal some other element in s?
    >>> all_have_an_equal([-4,-3,-2, 3, 2, 4])
    False
    >>> all_have_an_equal([4,3,2,3,2,4])
    True
    """
    # build a list contain every element except s[i]
    for i in range(len(s)):
        if s[i] not in s[:i] + s[i+1:]:
            return False
    return True

# use all() + slicing
def all_have_an_equal2(s):
    """>>> all_have_an_equal2([-4,-3,-2, 3, 2, 4])
    False
    >>> all_have_an_equal2([4,3,2,3,2,4])
    True
    """
    return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])

print(all_have_an_equal2([-4,-3,-2, 3, 2, 4]))

# use(sum())

def all_have_equal3(s):
    times = [sum(1 for y in s if y == x) for x in s]
    return all([i > 1 for i in times])
# one line
"""
all([sum(1 for y in s if y == x) > 1 for x in s])
or 
min([sum(1 for y in s if y == x) for x in s]) > 1 
or 
min([s.count(x) for x in s]) > 1
"""
