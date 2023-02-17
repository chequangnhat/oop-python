from .Account import Account


class SavingAccount(Account):   
  def __init__(self, account_number,  balance=0):
      super().__init__(account_number, balance)

