#!/usr/bin/env python3

import random

def gen_player_achievements() -> set :
    list_achievements = ["sword_master", "ninja", "gunslinger", "brawler", "berserker", "first_blood", "tank" ,"survivor", "speedrunner", "explorer", "pacifist", "header", "luck_strike"]
    player = random.randint(1, len(list_achievements))
    player_achievements = random.sample(list_achievements, player)

    return set(player_achievements)

if __name__ == "__main__" :
    print("=== Achievement Tracker System ===")

    players = {
        "Alice" : gen_player_achievements(),
        "Bob" : gen_player_achievements(),
        "Charlie" : gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, achievements in players.items() :
        print(f"{name} achievements: {achievements}")

    all_achievement = set.union(*players.values())
    print(f"\nAll distinct achievements: {all_achievement}")
    print(f"Common achievements: {set.intersection(*players.values())}")

    print("\n")

    for name, achievements in players.items() :
        others = set()
        for others_name, others_achievements in players.items() :
            if others_name != name :
                others = others.union(others_achievements)
        print(f"Only {name} has: {achievements.difference(others)}")

    print("\n")
    for name, achievements in players.items() :
        print(f"{name} is missing: {all_achievement.difference(achievements)}")
