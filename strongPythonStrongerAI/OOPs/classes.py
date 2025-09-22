class Dog:
    def __init__(self, name=None, age=None):
        self.name = name   # attribute
        self.age = age
    
    def bark(self):       # method
        print(f"{self.name} says woof!")

my_dog = Dog("Bruno", 3)
my_dog.bark()
