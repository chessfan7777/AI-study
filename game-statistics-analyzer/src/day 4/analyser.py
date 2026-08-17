import csv
import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_DIR / "data" / "game-sessions.csv"
OUTPUT_FILE = PROJECT_DIR / "output" / "summary.json"


def load_games():
    games = []

    with open(DATA_FILE, newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            game = {
                "game_id": row["game_id"],
                "kills": int(row["kills"]),
                "deaths": int(row["deaths"]),
                "accuracy": float(row["accuracy"])
                if row["accuracy"] != ""
                else None
            }

            games.append(game)

    return games


def calculate_statistics(games):
    total_games = len(games)

    total_kills = sum(game["kills"] for game in games)
    total_deaths = sum(game["deaths"] for game in games)

    valid_accuracies = [
        game["accuracy"]
        for game in games
        if game["accuracy"] is not None
    ]

    missing_accuracy_count = total_games - len(valid_accuracies)

    average_kills = total_kills / total_games
    average_deaths = total_deaths / total_games
    average_accuracy = sum(valid_accuracies) / len(valid_accuracies)

    return {
        "total_games": total_games,
        "average_kills": average_kills,
        "average_deaths": average_deaths,
        "average_accuracy": average_accuracy,
        "missing_accuracy_count": missing_accuracy_count
    }


def find_best_game(games):
    best_game = games[0]

    for game in games[1:]:
        if game["kills"] > best_game["kills"]:
            best_game = game

        elif game["kills"] == best_game["kills"]:
            if (
                game["accuracy"] is not None
                and best_game["accuracy"] is not None
                and game["accuracy"] > best_game["accuracy"]
            ):
                best_game = game

    return best_game


def find_worst_game(games):
    worst_game = games[0]

    for game in games[1:]:
        if game["kills"] < worst_game["kills"]:
            worst_game = game

        elif game["kills"] == worst_game["kills"]:
            if (
                game["accuracy"] is not None
                and worst_game["accuracy"] is not None
                and game["accuracy"] < worst_game["accuracy"]
            ):
                worst_game = game

    return worst_game


def save_summary(statistics):
    OUTPUT_FILE.parent.mkdir(exist_ok=True)

    summary = {
        "total_games": statistics["total_games"],
        "average_kills": round(statistics["average_kills"], 2),
        "average_deaths": round(statistics["average_deaths"], 2),
        "average_accuracy": round(statistics["average_accuracy"], 2),
        "missing_accuracy_count": statistics["missing_accuracy_count"]
    }

    with open(OUTPUT_FILE, "w") as file:
        json.dump(summary, file, indent=4)


def main():
    games = load_games()

    statistics = calculate_statistics(games)

    best_game = find_best_game(games)
    worst_game = find_worst_game(games)

    print(f"Games analyzed: {statistics['total_games']}")
    print(f"Average kills: {statistics['average_kills']:.2f}")
    print(f"Average deaths: {statistics['average_deaths']:.2f}")
    print(f"Average accuracy: {statistics['average_accuracy']:.2f}%")
    print(f"Best game: {best_game['game_id']}")
    print(f"Worst game: {worst_game['game_id']}")
    print(
        f"Missing accuracy values: "
        f"{statistics['missing_accuracy_count']}"
    )

    save_summary(statistics)


if __name__ == "__main__":
    main()