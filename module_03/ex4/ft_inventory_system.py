#!/usr/bin/env python3

import sys

def display_inventory(inventory) :
    print("=== inventory ===")

    for item in inventory :
        print(f"{item} : {inventory[item]}")


def main() :
    inventory = {}

    print("=== Inventory Master ===")

    for argument in sys.argv[1:] :
        parts_argument = argument.split(":")

        if len(parts_argument) != 2 :
            print(f"Error: Invalid format: {argument}")
            continue

        item_name = parts_argument[0]
        value_name = parts_argument[1]
        if item_name == "" or value_name == "":
            print(f"Error: invalid format: {argument}")
            continue

        try :
            quantity = int(value_name)
        except ValueError :
            print(f"Error: invalid quantity: {argument}")
            continue

        if item_name in inventory :
            print(f"Error: duplicate item : {item_name}")
            continue

        inventory[item_name] = quantity

    if len(inventory) == 0:
        print("No valid items")
        return

    display_inventory(inventory)


    print("\n=== Item List")
    items_list = list(inventory.keys())
    print(f"{items_list}")


    total_quantity = sum(inventory.values())
    print("\n === Total Quantity ===")
    print(f"{total_quantity}")

    print("\n === item percentages ===")
    for item in inventory:
        percentage = inventory[item] / total_quantity * 100
        percentage = round(percentage, 2)
        print(f"{item}: {percentage}%")


if __name__ == "__main__" :
    main()
