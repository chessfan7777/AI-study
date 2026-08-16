import csv

with open("data/game-sessions.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["game_id"], row["kills"])