class Stocks:
    def __init__(self):
        self.stockDict = {}
        self.__balance: float = 0

    def deposit(self,amount):
        self.__balance += amount

    def showBalance(self):
        print("balance: ",self.__balance)

    def buyStock(self, name: str, price: int):
        if self.__balance >= price:
            if name in self.stockDict:
                print(f"{name} already in stock list.")
            else:
                self.stockDict[name] = price
                print(f"Stock named {name} is bought at Rs. {price}.")
                self.__balance -= price
        else: print(f"You don't have enough money to buy {name} stock.")

    def sellStock(self, name: str):
        if name in self.stockDict:
            price = self.stockDict[name]
            self.__balance += price
            del self.stockDict[name]
            print(f"Stock {name} sold successfully.")
        else:
            print(f"Stock {name} not found.")

trader = Stocks()
trader.buyStock("google",1000)
trader.deposit(10000)
trader.showBalance()
trader.buyStock("google",4000)
trader.showBalance()
trader.buyStock("amazon",4000)
trader.showBalance()
trader.buyStock("openai",3000)
trader.showBalance()
trader.sellStock("amazon")
trader.showBalance()
trader.buyStock("openai",3000)
trader.showBalance()

class Variables:
    def __init__(self,name,age,bank_balance):
        self.name = name
        self._age = age
        self.__balance = bank_balance

a = Variables("name",19,1000)
print(a.name)
print(a._age)
print(a.__balance)