# Inheritance Override
class Account:
    def __init__(self, name, acc_no, balance):
        self.acc_name = name
        self.acc_no = acc_no
        self.acc_balance = balance

    def deposit(self, amount):
        self.acc_balance += amount

    def withdraw(self, amount):
        if amount > self.acc_balance:
            print(f"Insufficient funds. Balance is {self.acc_balance}")
        else:
            self.acc_balance -= amount


acc1 = Account("Jude", "0001", 12900)
acc1.deposit(100)
print(acc1.acc_balance)

acc2 = Account(balance=580, name="Ibaks", acc_no="0002")  # using named parameters
acc2.deposit(20)
print(acc2.acc_balance)
