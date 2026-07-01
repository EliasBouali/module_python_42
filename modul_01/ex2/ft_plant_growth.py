#!/usr/bin/env python3

class Plant :
    def __init__(self, name, height, age, growth_rate):
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
    rose = Plant("Rose", 25.0, 30, 0.8)

    initial_height = rose.height

    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 7 + 1) :
        print(f"=== Day {i} ===")
        rose.age_grow()
        rose.grow()
        rose.show()

    growth = rose.height - initial_height
    print(f"Growth this week: {round(growth, 1)}cm")
