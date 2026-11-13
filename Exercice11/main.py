class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            print("Montant invalide.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Retrait impossible.")

    def display_balance(self):
        print(f"{self.account_holder} : {self.balance} €")


account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(500)
account.display_balance()
