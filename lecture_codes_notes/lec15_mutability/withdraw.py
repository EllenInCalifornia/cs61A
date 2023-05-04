# mutable values can be used to define mutable functions
# mutable values & persistent local state

def make_withdraw_list(n):

    """
    >>> withdraw = make_withdraw_list(100)
    >>> withdraw(20)
    80
    >>> withdraw(20)
    60
    >>> withdraw(80)
    'insufficient'
    >>> withdraw(20)
    40
    """
    balance = [n]
    def withdraw(amount):
        if amount > balance[0]:
            return "insufficient"
        balance[0] = balance[0] - amount
        return balance[0]

    return withdraw

