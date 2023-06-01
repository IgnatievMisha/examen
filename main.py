class BankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    def deposit(self):
        self.balance = self.balance + 100
        print(self.balance)
    def withdraw(self):
        self.balance = self.balance - 100
        if self.balance>0:
            print(self.balance)
bank=BankAccount(balance = 1000, account_number = 777)
bank.deposit()
bank.withdraw()