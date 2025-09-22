class Person:
    def __init__(self,name=None,age=None) -> None:
        self.name = name
        self.age = age
    
    def intro(self):
        print(f"Name: {self.name}\tAge: {self.age}")
    
class Teacher(Person):
    def __init__(self, name, age,salary) -> None:
        super().__init__(name, age)
        self.salary = salary

    def intro(self):
        print(f"Name: {self.name}\tAge: {self.age}\t\tSalary: {self.salary}")

p = Person('ram',28)
p.intro()

t = Teacher("hari",34,35499.97)
t.intro()