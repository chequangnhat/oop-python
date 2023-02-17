import os

class Bank:
 
  def run(self, customer):
    while True:
      print("\n\t\t******** DIGITAL BANK ********\n")
      print("""\n1. Thong tin khach hang\n2. Them tai khoan ATM\n3. Them tai khoan tin dung\n4. Rut tien\n5. Lich su giao dich\n0. thoat\n""")
      choose = int(input("enter choose: "))

      match choose:
        case 1:
          os.system('cls')
          print("thong tin khach hang")
          customer.get_info()
        case 2:
          os.system('cls')
          print("them tai khoan ATM")
          customer.add_saving_account()
        case 3:
          os.system('cls')
          print("them tai khoan tin dung")
          customer.add_loan_account()
        case 4:
          os.system('cls')
          print("rut tien")
          customer.with_draw()
        case 5:
          os.system('cls')
          print("lich su giao dich")
          customer.show_transaction_history()
        case 0:
          os.system('cls')
          print("da thoat ung dung")
          break
        case default:
          os.system('cls')
          print("nhap sai")

