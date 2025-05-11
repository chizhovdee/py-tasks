import json


def save_game(filename, game_data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(game_data, f, ensure_ascii=False, indent=2)


def load_game(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
