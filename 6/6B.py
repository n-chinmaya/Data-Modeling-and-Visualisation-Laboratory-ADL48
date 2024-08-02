class Bank:
    def __init__(self, balance):
        if balance <= 0:
            raise ValueError("Balance must be greater than zero")
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

bank = Bank(1000)
bank.deposit(500)
bank.withdraw(200)
bank.check_balance()
bank.withdraw(2000) #Error