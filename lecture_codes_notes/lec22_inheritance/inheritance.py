from instanceAttribute import *


class CheckingAccount(Account):
    """A bank account that charges for withdrawls"""
    withdraw_fee = 1
    interest = 0.01

    def withdraw(self, amount):
        # syntax: pass self as the parameter
        return Account.withdraw(self, amount + self.withdraw_fee)
