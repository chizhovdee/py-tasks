import random
from settings import TILES


def ignite_random_trees(game_map, count):
    height = len(game_map)
    width = len(game_map[0])

    candidates = [
        (y, x)
        for y in range(height)
        for x in range(width)
        if game_map[y][x] == TILES["tree"]
    ]

    trees_to_burn = random.sample(candidates, min(count, len(candidates)))

    for y, x in trees_to_burn:
        game_map[y][x] = TILES["fire"]
