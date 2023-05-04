def palindrome(s):
    return list(reversed(s)) == list(s)

def palindrome(s):
    return all([a == b for a, b in zip(s, reversed(s))])
palindrome('seveneves')

