import random
from settings import TILES


def place_hospital(game_map):
    height = len(game_map)
    width = len(game_map[0])
    while True:
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)
        if game_map[y][x] == TILES["ground"]:
            game_map[y][x] = TILES["hospital"]
            return (y, x)
