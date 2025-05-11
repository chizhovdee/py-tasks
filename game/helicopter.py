from settings import TILES
import random


class Helicopter:
    def __init__(self, game_map):
        self.y = 0
        self.x = 0
        self.find_start_position(game_map)

    def find_start_position(self, game_map):
        height = len(game_map)
        width = len(game_map[0])
        while True:
            y = random.randint(0, height - 1)
            x = random.randint(0, width - 1)
            if game_map[y][x] == TILES["ground"]:
                self.y, self.x = y, x
                break

    def move(self, direction, game_map):
        dy, dx = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}.get(
            direction, (0, 0)
        )

        new_y = self.y + dy
        new_x = self.x + dx

        if 0 <= new_y < len(game_map) and 0 <= new_x < len(game_map[0]):
            self.y, self.x = new_y, new_x

    def draw(self, game_map):
        game_map[self.y][self.x] = TILES["helicopter"]
