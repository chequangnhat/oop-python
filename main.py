from classes.Bank import Bank
from classes.Customer import Customer

def main():
  customer = Customer("01", "nhat", "premium")
  digitalBank = Bank()
  digitalBank.run(customer)

main()