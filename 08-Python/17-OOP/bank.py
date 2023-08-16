# INITIALIZE THE CLASS
class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
 
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
 
    def display(self):
        print("\n New Available Balance =", self.balance)
  
# CREATING BANK ACCOUNT OBJECT
s = Bank_Account()
  
# CALLING THE FUNCTION WITHIN THE BANK CLASS
s.deposit()
s.withdraw()
s.display()