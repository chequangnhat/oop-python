from .SavingAccount import SavingAccount
from .LoanAccount import LoanAccount

from rich.console import Console
from rich.table import Table

from datetime import datetime

class Customer:
  list_accounts = []
  transaction_history = []
  def __init__(self, id, name, rank ):
    self.id = id
    self.name = name
    self.rank = rank

  def add_saving_account(self):
    account_number = input("enter account number: ")
    account_balance = input("enter account balance: ")

    new_account = SavingAccount(account_number, account_balance)
    self.list_accounts.append(new_account)

  def add_loan_account(self):
    account_number = input("enter account number: ")
    account_balance = input("enter account balance: ")

    new_account = LoanAccount(account_number, account_balance)
    self.list_accounts.append(new_account)

  def get_total_balance(self):
    sum = 0
    for account_index in range(len(self.list_accounts)):
      sum += float(self.list_accounts[account_index].balance)
    return sum

  def check_type_account(self, account):
    if isinstance(account, SavingAccount):
      return "saving account"
    if isinstance(account, LoanAccount):
      return "loan account"

  def get_info(self):
    total_balance = self.get_total_balance()
    table = Table(title="thong tin khach hang", show_header=False,expand=True)
    table.add_row(str(self.id), str(self.name),str(self.rank), "{:,.0f}đ".format(total_balance))

    if not len(self.list_accounts) == 0:
      for account in self.list_accounts:
        table.add_row(str(account.account_number), str(self.check_type_account(account)),"", "{:,.0f}đ".format(account.balance))
    
    console = Console()
    console.print(table)

  def find_account(self, account_number):
    for account_index in range(0,len(self.list_accounts)):
      if self.list_accounts[account_index].account_number == account_number:
        return account_index
    return -1

  def with_draw(self):
    saving_accounts = filter(lambda account: isinstance(account, SavingAccount), self.list_accounts)
    table = Table(title="thong tin account",expand=True)
    table.add_column("index")
    table.add_column("number")
    table.add_column("balance")
    index = 0
    for account in saving_accounts:
      table.add_row(str(index), str(account.account_number), str(account.balance))
      index+=1

    console = Console()
    console.print(table)
    choose_account_number = input("Choose account number: ")
    amount = float(input("Enter amount: "))

    transaction_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    founded_account = self.list_accounts[self.find_account(choose_account_number)]
    founded_account.withdraw(amount*1.01)
    self.transaction_history.append({"amount": amount, "balance": founded_account.balance,"account_number": choose_account_number, "transaction_time": str(transaction_time)})

    table1 = Table(title="BIEN LAI GIAO DICH", show_header=False,expand=True)
    table1.add_row("NGAY G/D", str(transaction_time))
    table1.add_row("ATM ID", "DIGITAL-BANK-ATM 2023")
    table1.add_row("SO TK", str(choose_account_number))
    table1.add_row("SO TIEN", "{:,.0f}đ".format(amount))
    table1.add_row("SO DU", "{:,.0f}đ".format(founded_account.balance))
    table1.add_row("PHI + VAT", "{:,.0f}đ".format(amount*0.01))
    console.print(table1)

    hold = input("enter any key to return")

  def show_transaction_history(self):
    self.get_info()

    console = Console()
    table = Table(title="lich su giao dich", show_header=False,expand=True)
    for history in self.transaction_history:
      table.add_row(f"[G/D] {history['account_number']}", "{:,.0f}đ".format(history['amount']), history["transaction_time"])
    console.print(table)






