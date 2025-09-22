from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        print("Roar !!!")
    # pass

simba = Lion()
simba.sound()