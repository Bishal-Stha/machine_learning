#Classes and Objects
class Student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def myIntro(self):
        print(f"my name is {self.name} and I am {self.age} years.")

s1 = Student("Bishal",18)
s1.myIntro()

class Book:
    def __init__ (self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def aboutBook(self):
        print(f"The title of this book is {self.title}. It was written by {self.author} and it costs just Rs {self.price}.")
    

# Inheritance
class Poem(Book):
    def __init__(self,title, author, price,theme):
        # self.title = title
        # self.author = author
        # self.price = price
        super().__init__(title,author,price) #calls above 3 commented lines.
        self.theme = theme

    def aboutTheme(self):
        print(f"The book is about {self.theme}.")

    def aboutBook(self):
        super().aboutBook()
        print(f"The theme of this book is {self.theme}.")

b1 = Book("Sacrifical Lamb","Victor Timely",580)
p1 = Poem("The GOAT","Alexander Coprenius",899,"Survival")

b1.aboutBook()
p1.aboutTheme()
p1.aboutBook()

#Encapsulation
class Bank:
    def __init__ (self):
        self.__balance =0 #now, balance is a private variable
    
    def set_balance(self,amount):
        self.__balance +=amount

    def get_balance(self):
        return self.__balance


axis_bank =Bank()#this does work
# axis_bank.set_balance
print(axis_bank.get_balance())
axis_bank.set_balance(12345)
print(f"Bank balance: {axis_bank.get_balance()}")