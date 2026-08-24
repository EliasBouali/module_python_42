#!/usr/bin/env python3
from typing import Generator
import random


def gen_event() -> Generator :
    name_list = ["zoro", "luffy", "sun", "sacha"]
    action_list = ["sabreur", "capitain", "chasseur", "dresseur"]

    while True :
        name_choice = random.choice(name_list)
        action_choice = random.choice(action_list)
        yield name_choice, action_choice

def consume_event(liste : list) -> Generator :
    while liste :
        liste_choice = random.choice(liste)
        liste.remove(liste_choice)
        yield liste_choice

if __name__ == "__main__" :
    gen = gen_event()

    print("=== Game Data Stream Processor ===")
    for i in range(1000) :
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    event_list = []

    for i in range(10) :
        event_list.append(next(gen))

    print(event_list)

    for event in consume_event(event_list) :
        print(f"Got event from list : {event}")
        print(f"Remains in list: {event_list}")
