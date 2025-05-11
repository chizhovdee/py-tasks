import random
from settings import TILES


def generate_trees(game_map, count):
    height = len(game_map)
    width = len(game_map[0])

    placed = 0
    while placed < count:
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)

        if game_map[y][x] == TILES["ground"]:
            game_map[y][x] = TILES["tree"]
            placed += 1
