#!/usr/bin/env python3
import math


def get_player_spot() :
    while True :
        coordonates = input("Enter new coordinates as floats in format 'x,y,z': ")
        try :
            parties = coordonates.split(",")
            if len(parties) != 3 :
                raise ValueError("Need exactly 3 coordinates")
            x = float(parties[0])
            y = float(parties[1])
            z = float(parties[2])

            return (x, y, z)
        except ValueError as error :
            print("Invalid input, try again")


if __name__ == "__main__" :
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    pos1 = get_player_spot()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")
    distance = round(math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2), 4)
    print(f"Distance to center: {distance}")

    print("Get a second set of coordinates")
    pos2 = get_player_spot()
    distance_2 = round(math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1])**2 + (pos2[2] - pos1[2]) **2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance_2}")
