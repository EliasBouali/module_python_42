#!/usr/bin/env python3

import sys


if __name__ == "__main__" :

    score_liste = []
    print("=== Player Score Analytics ===")
    for i in range(1, len(sys.argv)) :
        try :
            number = int(sys.argv[i])
            score_liste.append(number)
        except ValueError as error :
            print("Invalid score ignored")

    if len(score_liste) == 0 :
             print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else :
            print(f"Score processed: {score_liste}")
            print(f"Total players: {len(score_liste)}")
            print(f"Total score: {sum(score_liste)}")
            print(f"Average score: {round(sum(score_liste) / len(score_liste), 2)}")
            print(f"High score: {max(score_liste)}")
            print(f"Low score: {min(score_liste)}")
            print(f"Score range: {max(score_liste) - min(score_liste)}")
