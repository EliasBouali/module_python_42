#!/usr/bin/env python3

class Plant :

    class Stats :
        def __init__(self) :
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def grow(self) :
            self._grow_count += 1

        def age(self) :
            self._age_count += 1

        def show_called(self) :
            self._show_count += 1

        def display(self, name) :
            print(f"Stats for {name}:")
            print(f"grow() calls : {self._grow_count}")
            print(f"age() calls : {self._age_count}")
            print(f"show() calls : {self._show_count}")

    def __init__(self, name, height, age, growth_rate=0.8):
        self.name = name
        self.set_height(height, verbose=False)
        self.set_age(age, verbose=False)
        self.growth_rate = growth_rate
        self._stats = Plant.Stats()

    def display_stats(self) :
        self._stats.display(self.name)

    def show(self) :
        self._stats.show_called()
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
        self._stats.age()

    def grow(self) :
        self._height = round(self._height + self.growth_rate, 1)
        self._stats.grow()

    @staticmethod
    def is_older_than_a_year(age) :
        if age <= 365 :
            return False
        return True

    @classmethod
    def create_anonymous_plant(cls) :
        return cls("Unknown", 0.0, 0)


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

class Seed(Flower) :
    def __init__(self,name, height, age, color) :
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def bloom(self) :
        super().bloom()
        self.seed_count = 10

    def show(self) :
        super().show()
        print(f"Seed count: {self.seed_count}")

class Tree(Plant) :

    class Tree_Stats(Plant.Stats) :
        def __init__(self) :
            super().__init__()
            self._produce_shade_count = 0

        def produce_shade(self) :
            self._produce_shade_count += 1

        def display(self, name) :
            super().display(name)
            print(f"produce_shade() calls: {self._produce_shade_count}")

    def __init__(self, name, height, age, trunk_diameter) :
        super().__init__(name, height, age)
        self._stats = Tree.Tree_Stats()
        self.trunk_diameter = trunk_diameter

    def show(self) :
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) :
        self._stats.produce_shade()
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


def display_plant_stats(plant) :
    plant.display_stats()



if __name__ == "__main__" :
    print("=== Garden Analytics ===")

    print("\n=== Static method test ===")
    print(f"Is 30 days older than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days older than a year? -> {Plant.is_older_than_a_year(400)}")

    print("\n=== Anonymous Plant ===")
    anonymous = Plant.create_anonymous_plant()
    anonymous.show()
    display_plant_stats(anonymous)

    print("\n=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("\n=== Seed ===")
    seed = Seed("Sunflower", 10.0, 5, "yellow")
    seed.show()
    seed.bloom()
    seed.show()
    display_plant_stats(seed)

    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    oak.produce_shade()
    oak.produce_shade()
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Is Oak older than a year? ===")
    print(f"-> {Plant.is_older_than_a_year(oak.get_age())}")
