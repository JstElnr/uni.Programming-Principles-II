class Account:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def check_cash(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
ba1 = Account("Kairat")
ba2 = Account("Nurtas")
ba1.check_cash()
ba1.withdrawal(100)
ba1.deposit(500)
ba1.withdrawal(200)
