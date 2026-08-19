import csv
import json
import os

total_games = 0
total_kills = 0
total_deaths = 0

total_accuracy = 0
valid_accuracy_count = 0
missing_accuracy_count = 0


with open("data/game-sessions.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_games += 1

        total_kills += int(row["kills"])
        total_deaths += int(row["deaths"])

        # Accuracy can be blank
        if row["accuracy"] != "":
            total_accuracy += float(row["accuracy"])
            valid_accuracy_count += 1
        else:
            missing_accuracy_count += 1


# Calculate averages
average_kills = total_kills / total_games
average_deaths = total_deaths / total_games
average_accuracy = total_accuracy / valid_accuracy_count


# Print results
print(f"Total games: {total_games}")
print(f"Average kills: {average_kills:.2f}")
print(f"Average deaths: {average_deaths:.2f}")
print(f"Average accuracy: {average_accuracy:.2f}%")
print(f"Missing accuracy values: {missing_accuracy_count}")


# Make sure output folder exists
os.makedirs("output", exist_ok=True)


# Create the data that will go into the JSON file
summary = {
    "total_games": total_games,
    "average_kills": round(average_kills, 2),
    "average_deaths": round(average_deaths, 2),
    "average_accuracy": round(average_accuracy, 2),
    "missing_accuracy_count": missing_accuracy_count
}


# Write summary.json
with open("output/summary.json", "w") as file:
    json.dump(summary, file, indent=4)