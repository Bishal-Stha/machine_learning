class Microwave:
    def __init__(self, brand:str, power_rating: str, price: float) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.price = price
        self.turned_on = False

    def turn_on(self) -> None:
        if self.turned_on:
            print(f"Microwave ({self.brand}) is already turned on.")
        else:
            print(f"Microwave ({self.brand}) is now turned on.")
            self.turned_on = True

    def turn_off(self) -> None:
        if self.turned_on == True:
            print(f"Microwave ({self.brand}) is now turned off.")
            self.turned_on = False
        
        else:
            print(f"Microwave ({self.brand}) is already turned off.")

    def about_microwave(self) -> None:
        print(f"Brand: {self.brand}")
        print(f"Power rating: {self.power_rating}")
        print(f"Price: {self.price}")

    # Dunder methods: Double underscore
    def __str__(self) -> str:
        return f"Microwave(Brand: {self.brand}, Power rating: {self.power_rating}, Price: {self.price})"
    
    def __repr__(self) -> str:
        return f'Microwave(brand="{self.brand}", power_rating="{self.power_rating}", price={self.price})'

bishal: Microwave = Microwave(brand="Good Life", power_rating="14 KW", price=4500.45) # :Microwave is a type annotation. Not including type annotation will not necessarily give an error but its a good practice.

# bishal.about_microwave()
# bishal.about_microwave()
# bishal.turn_on()
# bishal.turn_off()
print(bishal) ## Its fancy way of showing the class content. makes it easily readable for even a 90 year old.
print(repr(bishal)) ## Helpful for users to see what does the class contain. easy to read and get a good idea about the datatypes of attributes of the class.