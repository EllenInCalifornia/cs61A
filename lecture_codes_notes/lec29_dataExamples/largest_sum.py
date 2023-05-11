def largest_adj_sum(s):
    """the largest sum of two adjacent elements in a list s
    assume len(s) > 1
    >>> largest_adj_sum([-4,-3,-2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3,-2,-3, 2,-4])
    1
    """
    largest_sum = s[0] + s[1]
    i = 2
    while i < len(s):
        largest_sum = max(largest_sum, s[i - 1] + s[i])
        i += 1
    return largest_sum

#  老师的方法
def largest_adj_sum1(s):
    """the largest sum of two adjacent elements in a list s
    assume len(s) > 1
    >>> largest_adj_sum1([-4,-3,-2, 3, 2, 4])
    6
    >>> largest_adj_sum1([-4, 3,-2,-3, 2,-4])
    1
    """
    adj_sum_list = [s[i] + s[i + 1] for i in range(len(s)-1)]
    return max(adj_sum_list)

# 好妙的zip
def largest_adj_sum_zip(s):
    """the largest sum of two adjacent elements in a list s
    assume len(s) > 1
    >>> largest_adj_sum_zip([-4,-3,-2, 3, 2, 4])
    6
    >>> largest_adj_sum_zip([-4, 3,-2,-3, 2,-4])
    1
    """
    pairs = zip(s[1:], s[:-1])
    adj_sum_list = [sum(t) for t in pairs]
    return max(adj_sum_list)
