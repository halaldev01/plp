# Base class
class Superhero:
    def __init__(self, name, power, strength):
        self.__name = name         # Encapsulation: private attribute
        self.power = power
        self.strength = strength

    def get_name(self):
        return self.__name

    def show_stats(self):
        print(f"{self.get_name()} has the power of {self.power} and strength {self.strength}.")

# Inheritance: A specialized superhero
class FlyingHero(Superhero):
    def fly(self):
        print(f"{self.get_name()} is flying high in the sky! ✈️")

# Inheritance: Another specialized superhero
class StrongHero(Superhero):
    def lift_heavy_object(self):
        print(f"{self.get_name()} is lifting a car with ease! 🚗")

# Creating objects
hero1 = FlyingHero("SkyMan", "Flight", 80)
hero2 = StrongHero("MightyMan", "Super Strength", 95)

# Using methods
hero1.show_stats()
hero1.fly()

hero2.show_stats()
hero2.lift_heavy_object()
