#!/usr/bin/env python3

class Plant :
    def __init__(self, name, height, age, growth_rate=0.8):
        self.name = name
        self.set_height(height, verbose=False)
        self.set_age(age, verbose=False)
        self.growth_rate = growth_rate

    def show(self) :
        print(f"{self.name}: {self._height}cm, {self._age} days old")


    def set_height(self, height_value, verbose=True) :
        if height_value < 0 :
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else :
            self._height = height_value
            if verbose :
                print(f"Height updated: {height_value}cm")

    def set_age(self, age_value, verbose=True) :
        if age_value < 0 :
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else :
            self._age = age_value
            if verbose :
                print(f"Age updated: {age_value} days")

    def get_height(self) :
        return self._height

    def get_age(self) :
        return self._age

    def age_grow(self) :
        self._age += 1

    def grow(self) :
        self._height = round(self._height + self.growth_rate, 1)


class Flower(Plant) :
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) :
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed :
            print(f"{self.name} is blooming beautifully!")
        else :
            print(f"{self.name} has not bloomed yet")

class Tree(Plant) :
    def __init__(self, name, height, age, trunk_diameter) :
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) :
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) :
        print(f"Tree {self.name} now produces a shade of {self._height}cm long and {self.trunk_diameter}cm wide.")


class Vegetable(Plant) :
    def __init__(self, name, height, age, harvest_season) :
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def show(self) :
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def age_grow(self) :
        super().age_grow()
        self.nutritional_value += 0.5

    def grow(self):
        super().grow()
        self.nutritional_value += 0.5


if __name__ == "__main__" :
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20) :
        tomato.grow()
        tomato.age_grow()
    tomato.show()
