print("Welcome to Chase bank.")
print("Have a nice day!")


class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= int(amount)
        print("your current balance is: "+str(self.balance))

    def deposit(self, amount):
        self.balance += int(amount)
        print("your current balance is: "+str(self.balance))

    def check(self):
        print("your current balance is: "+str(self.balance))


task = input("what would you like to do(withdraw, deposit, balance")

person = Bank("john", 1000)

if task == "withdraw":
    amount = input("what is the amount?")
    person.withdraw(amount)
if task == "deposit":
    amount = input("what is the amount?")
    person.deposit(amount)
if task == "balance":
    person.check()
