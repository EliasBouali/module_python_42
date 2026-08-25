#!/usr/bin/env python3
import random

print("=== Game Data Alchemist ===")

name_list = ["Alice", "bob", "Charlie", "dylan", "Emma", "gregory", "Liam", "john", "Sarah", "kevin"]
print(f"Initial list of players: {' ,'.join(name_list)}")

all_capitalized = [name.capitalize() for name in name_list]
print(f"\nNew list with all names capitalized : {' ,'.join(all_capitalized)}")

capitalize_list = [name for name in name_list if name[0].isupper()]
print(f"\nNew list of capitalized names only: {' ,'.join(capitalize_list)}")

score_dict = {name: random.randint(0, 100) for name in all_capitalized }
print(f"\n Score dict: {score_dict}")

average_score = sum(score_dict.values()) / len(score_dict)
print(f"\nScore average is {average_score}")

high_scores = {name: valeur for name, valeur in score_dict.items() if valeur > average_score}
print(f"High scores: {high_scores}")
