import random
from settings import TILES


def generate_rivers(game_map, count):
    height = len(game_map)
    width = len(game_map[0])
    section_height = height // count

    for i in range(count):
        # выбираем направление
        direction = random.choice(["horizontal", "vertical"])
        section_start = i * section_height
        section_end = min(height, (i + 1) * section_height)

        if direction == "horizontal":
            y = random.randint(section_start, max(section_start, section_end - 1))
            x_start = random.randint(0, width - 5)
            length = random.randint(4, 6)
            for dx in range(length):
                x = x_start + dx
                if x < width and game_map[y][x] == TILES["ground"]:
                    game_map[y][x] = TILES["water"]
        else:
            x = random.randint(0, width - 1)
            y_start = random.randint(section_start, max(section_start, section_end - 5))
            length = random.randint(4, 6)
            for dy in range(length):
                y = y_start + dy
                if y < height and game_map[y][x] == TILES["ground"]:
                    game_map[y][x] = TILES["water"]
