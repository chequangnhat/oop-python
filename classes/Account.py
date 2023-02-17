class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")

    def get_balance(self):
        return self.balance