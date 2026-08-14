player = [
    {
        "name": "Jerry",
        "kills": 14,
        "deaths": 12,
        "accuracy": 78
    },
    {
        "name": "Tom",
        "kills": 10,
        "deaths": 15,
        "accuracy": 65
    },
    {
        "name": "Harold",
        "kills": 1,
        "deaths": 1,
        "accuracy": 22
    },
    {
        "name": "JJ",
        "kills": 13,
        "deaths": 10,
        "accuracy": 45
    },
    {
        "name": "Sam",
        "kills": 44,
        "deaths": 3,
        "accuracy": 98
    },
    {
        "name": "Holt",
        "kills": 19,
        "deaths": 11,
        "accuracy": 89
    },
    {
        "name": "magnum",
        "kills": 120,
        "deaths": 1,
        "accuracy": 99
    },
    {
        "name": "Jake",
        "kills": 21,
        "deaths": 4,
        "accuracy": 78
    },
    {
        "name": "Plot",
        "kills": 99,
        "deaths": 0,
        "accuracy": 100
    },
    {
        "name": "Pam",
        "kills": 3,
        "deaths": 44,
        "accuracy": 2
    }
]

for p in player:
    print(f"Player: {p['name']}, Kills: {p['kills']}, Deaths: {p['deaths']}, Accuracy: {p['accuracy']}%")
    if p["deaths"] != 0:
        kd = p["kills"] / p["deaths"]
        print(f"K/D Ratio: {kd:.2f}")
    else:
        print("K/D Ratio: Infinity (No deaths)")
