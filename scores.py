import random
import csv


def random_scores() -> list:
    players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
    players_with_score = []

    for _ in range(100):
        for player in players:
            players_with_score.append({"Player": player, "Score": random.randint(0,1000)})
    return players_with_score


def write_to_file():
    with open('game_results.csv', 'w') as csv_file:
        fieldnames = ["Player", "Score"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        players_with_scores = random_scores()

        writer.writeheader()
        for el in players_with_scores:
            writer.writerow(el)

