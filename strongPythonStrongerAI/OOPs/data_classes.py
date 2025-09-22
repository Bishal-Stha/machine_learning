from dataclasses import dataclass

@dataclass
class Person:
    name:str
    age:int

person = Person("Bishal",19)
print(person,type(person))

@dataclass
class Student(Person):
    roll_no:int
    grade: str

    def display(self):
        print("Student Details")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Roll no: ",self.roll_no)
        print("Grade: ",self.grade)

std = Student("bishal",19,8,"Bachelor 1st year")
print(std)
std.display()


