from inheritance import *
from instanceAttribute import *
class Bank:
    """A bank *has* accounts
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    """
    def __init__(self):
        self.accounts = []
    def open_account(self, name, initial, type=Account):
        account = type(name, initial)
        self.accounts.append(account)
        return account
    def pay_interest(self):
        for account in self.accounts:
            account.deposit(account.balance * account.interest)


