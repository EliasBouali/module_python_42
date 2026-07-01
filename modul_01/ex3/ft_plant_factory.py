#!/usr/bin/env python3

class Plant :
    def __init__(self, name, height, age, growth_rate=0.8):
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def show(self) :
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def age_grow(self) :
        self.age += 1

    def grow(self) :
        self.height = round(self.height + self.growth_rate, 1)






if __name__ == "__main__" :
    rose = Plant("Rose", 25.0, 30)
    oak = Plant("Oak",200.0, 365)
    cactus = Plant("Cactus", 5.0, 90)
    sunflower = Plant("Sunflower", 80.0, 45)
    fern = Plant("Fern", 15.0, 120)

    print("=== Plant Factory Output ===")
    print("Created: ", end="")
    rose.show()
    print("Created: ", end="")
    oak.show()
    print("Created: ", end="")
    cactus.show()
    print("Created: ", end="")
    sunflower.show()
    print("Created: ", end="")
    fern.show()
