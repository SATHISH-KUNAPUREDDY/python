# class Bankaccount():
#     def __init__(self, Name,Account_no,ifsc_code,balance=0):
#          self.Name=Name
#          self.Account_no=Account_no
#          self.ifsc_code=ifsc_code
#          self.balance=balance
#     def deposit(self,amount):
#         if amount>0:
#             self.balance+= amount
#             return f"Deposited ${amount}. New balance:${self.balance}"
#         else:
#             return " Invalid amount deposited."
#     def withdraw(self,amount):
#         if 0<amount<self.balance:
#             self.balance-=amount
#             return f"Deposited ${amount}. New balance:${self.balance}"
#         else:
#             return "Insufficent funds or Invalid withdraw amount"
#     def balance_enquiry(self):
#         return f"Account holder:{self.Name}\nIFSC code:{self.ifsc_code}\nAccount no:{self.Account_no}\nBalance:{self.balance}"
    
# bank = Bankaccount("sathish","1235648901","HDFFI025",10)
# bank1 = Bankaccount("subbu","4561230787","SFIC8523",25)

# print(bank1.balance_enquiry())
# print(bank1.deposit(1000))
# print(bank1.withdraw(500))
