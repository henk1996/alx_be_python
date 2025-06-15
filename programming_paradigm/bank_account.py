class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        return (f"Deposited: ${self.account_balance}") 
    def withdraw(self, amount):
        if(self.account_balance < amount):
           return "Insufficient funds." 
        else:
           self.account_balance = self.account_balance - amount
           return (f"Withdrew: ${amount}")
    def display_balance(self):
        return (f"Current Balance: ${self.account_balance}")
