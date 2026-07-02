#!/usr/bin/env python3

def garden_operations(operation_nbr : int) :
    if operation_nbr == 0:
        int("abc")
    elif operation_nbr == 1:
        result = 10/0
    elif operation_nbr == 2:
        file = open("flowers.txt")
    elif operation_nbr == 3:
        result = "Rose" + 5
    else :
        return

def test_error_types() :

    print("=== Different exception Types ==")

    try :
        print("Testing operation 0...")
        garden_operations(0)
    except ValueError as error :
        print(f"Caught ValueError {error}")


    try :
        print("Testing operation 1...")
        garden_operations(1)
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")

    try :
        print("Testing operation 2...")
        garden_operations(2)
    except FileNotFoundError as error:
        print(f"Caught FileNotFounError: {error}")

    try :
        print("Testing operation 3...")
        garden_operations(3)
    except TypeError as error:
        print(f"Caught TypeError: {error}")

    try:
        print("Testing operation 4...")
        garden_operations(4)
        print("Operation completed successfully")
    except (ValueError, TypeError) as error:
        print(f"Caught one of multiple exceptions: {error}")



if __name__ == "__main__" :
    test_error_types()
