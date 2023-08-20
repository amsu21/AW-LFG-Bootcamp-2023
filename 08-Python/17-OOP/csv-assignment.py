class Bank:
    def __init__(self):
        self.balance = 0
        print("BANK MENU")
        print('''
    1. Deposit an amount into your account
    2. Withdraw an amount from your account
    3. Retrieve current balance
    4. See previous transactions
    5. Close Application''')
        
        def deposit(self):
            amount = float(input("Enter the amount to be Deposited: "))
            self.balance += amount
            print("\n Amount DepositedL ", amount)
        
        