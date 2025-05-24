from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self,owner):
        self.owner = owner
        self.balance =0

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass

    def showBalance(self):
        print(f"{self.owner}'s balance: {self.balance}")

class SavingAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner}'s bank balance: {self.balance}")
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"{self.owner}'s bank balance: {self.balance}")

bishal = SavingAccount("bishal shrestha")
bishal.deposit(75_000)
bishal.withdraw(50_000)
bishal.showBalance()