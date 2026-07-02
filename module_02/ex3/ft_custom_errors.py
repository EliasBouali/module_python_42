#!/usr/bin/env python3

class GardenError(Exception) :
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)

class PlantError(GardenError) :
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)

class WaterError(GardenError) :
    def __init__(self, message="Unknown water error"):
        super().__init__(message)

def check_garden() :
    raise GardenError("garden problem")

def check_plant() :
    raise PlantError("Plant error")

def check_water() :
    raise WaterError("Water error")


def test_custom_error() :
    print("===custom garden errors ===")

    try :
        check_garden()
    except GardenError as error :
        print(f"Caught GardenError: {error}")

    try :
        check_plant()
    except PlantError as error :
        print(f"Caught PlantError: {error}")

    try :
        check_water()
    except WaterError as error :
        print(f"Caught WaterError: {error}")

    try :
        check_plant()
    except GardenError as error :
        print(f"GardenError caught PlantError : {error}")

    try :
        check_water()
    except GardenError as error :
        print(f"GardenError caught WaterError: {error}")


if __name__ == "__main__" :
    test_custom_error()
