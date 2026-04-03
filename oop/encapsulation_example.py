# This program demonstrates encapsulation by using
# a private attribute and accessing it through methods.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance


    def deposit(self, amount):
        self.__balance += amount


    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(100)

account.deposit(50)
account.show_balance()
