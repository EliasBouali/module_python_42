#!/usr/bin/env python3

def input_temperature(temp_str: str) :
    temp_int = int(temp_str)
    return temp_int

def test_temperature() :
    print("=== Garden Temperature ===")

    print("Input data is '25'")
    try :
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error :
        print(f"Caught input_temperature error: {error}")

    print("Input data is 'abc'")
    try :
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error :
        print(f"Caught input temperature error: {error}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__" :
    test_temperature()
