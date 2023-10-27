class Account:
    def __init__(self, name, acc_no, balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance

    def print_balance(self):
        print(f"Balance for {self.acc_no} is ksh {self.balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


acc1 = Account("Calton", "0001", 1200)
acc2 = Account("Muriat", "0002", 12000)

acc1.deposit(600)
acc1.print_balance()

