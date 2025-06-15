class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
<<<<<<< HEAD
        print(f"Current Balance: ${self.account_balance:.2f}")
=======
        print(f"Current Balance: ${self.account_balance:.2f}")
>>>>>>> refs/remotes/origin/main
