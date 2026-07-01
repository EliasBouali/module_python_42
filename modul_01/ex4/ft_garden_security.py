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



if __name__ == "__main__" :


    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10, 0.8)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25.0)
    rose.set_age(30)
    rose.set_height(-1.0)
    rose.set_age(-5.0)
    print("Current state: ", end="")
    rose.show()
