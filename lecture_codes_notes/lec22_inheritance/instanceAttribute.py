class Account:
    interest = 0.02
    def __init__(self, holder, initial):
        self.holder = holder
        self.balance = initial

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def overdrawn(self):
        return self.balance < 0

    def __str__(self):
        return "balance: " + str(self.balance)
