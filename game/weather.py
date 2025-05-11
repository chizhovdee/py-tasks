import random
from settings import TILES


def generate_weather(game_map, weather_map, duration_ticks=100, cloud_count=15):
    height = len(game_map)
    width = len(game_map[0])
    weather_map.clear()

    positions = []

    while len(positions) < cloud_count:
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)
        if game_map[y][x] in [TILES["ground"], TILES["tree"], TILES["water"]]:
            positions.append((y, x))

    # 1/3 из них будут грозами
    storms = random.sample(positions, len(positions) // 3)

    for y, x in positions:
        tile = TILES["storm"] if (y, x) in storms else TILES["cloud"]
        weather_map[(y, x)] = {"type": tile, "timer": duration_ticks}
