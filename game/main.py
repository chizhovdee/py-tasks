import time
import os
import os.path
from pynput import keyboard
from savegame import save_game, load_game

from settings import TILES
from tree import generate_trees
from water import generate_rivers
from fire import ignite_random_trees
from helicopter import Helicopter
from shop import place_shop
from hospital import place_hospital
from weather import generate_weather

TICK_DELAY = 0.05
FIRE_LIFETIME = 150
WEATHER_UPDATE_TICKS = 100

current_key = None
save_requested = False


def on_press(key):
    global current_key, save_requested
    try:
        if key.char.lower() == "f":
            save_requested = True
        else:
            current_key = key.char.lower()
    except:
        pass


def create_empty_map(width, height):
    return [[TILES["ground"] for _ in range(width)] for _ in range(height)]


def print_map(game_map, water, water_capacity, lives, score):
    width = len(game_map[0])
    border_tile = "⬛"
    print(f"🪣 Вода: {water}/{water_capacity}   ❤️ Жизни: {lives}   ⭐ Очки: {score}\n")
    print(border_tile * (width + 2))
    for row in game_map:
        print(border_tile + "".join(row) + border_tile)
    print(border_tile * (width + 2))

    print("\n💡 Подсказки:")
    print(
        "❤️ +1 жизнь = 3 ⭐   |   🪣 +1 ёмкость воды = 5 ⭐   |   📅 Нажми F — сохранить игру"
    )


def main():
    global current_key, save_requested

    print("🌲 Игра: Тушение лесных пожаров 🌲")
    width = int(input("Введите ширину карты: "))
    height = int(input("Введите высоту карты: "))

    save_file = "save.json"
    load = False

    if os.path.exists(save_file):
        load = input("Загрузить сохранение? (y/n): ").lower() == "y"

    if load:
        data = load_game(save_file)
        game_map = data["game_map"]
        fire_timers = {
            tuple(map(int, k.split(","))): v for k, v in data["fire_timers"].items()
        }
        weather_map = {
            tuple(map(int, k.split(","))): v for k, v in data["weather_map"].items()
        }
        helicopter = Helicopter(game_map)
        helicopter.y, helicopter.x = data["helicopter"]
        water = data["water"]
        water_capacity = data["water_capacity"]
        lives = data["lives"]
        score = data["score"]
        tick = data["tick"]

        tree_count = sum(1 for row in game_map for cell in row if cell == TILES["tree"])
        if lives <= 0 or tree_count == 0:
            print("⚠️ Сохранение завершилось на GAME OVER — начинаем заново.")
            game_map = create_empty_map(width, height)
            generate_rivers(game_map, count=3)
            generate_trees(game_map, count=40)
            place_shop(game_map)
            place_hospital(game_map)
            helicopter = Helicopter(game_map)
            fire_timers = {}
            weather_map = {}
            generate_weather(game_map, weather_map)
            water = 0
            water_capacity = 1
            lives = 20
            score = 0
            tick = 0

    else:
        game_map = create_empty_map(width, height)
        generate_rivers(game_map, count=3)
        generate_trees(game_map, count=40)
        place_shop(game_map)
        place_hospital(game_map)
        helicopter = Helicopter(game_map)
        fire_timers = {}
        weather_map = {}
        generate_weather(game_map, weather_map)
        water = 0
        water_capacity = 1
        lives = 20
        score = 0
        tick = 0

    storm_cooldown = 0

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"🎮 Тик: {tick}")

        if tick % 5 == 0:
            active_fires = sum(
                1
                for y in range(height)
                for x in range(width)
                if game_map[y][x] == TILES["fire"]
            )
            fires_to_add = max(0, 2 - active_fires)
            if fires_to_add > 0:
                ignite_random_trees(game_map, count=fires_to_add)
                for y in range(height):
                    for x in range(width):
                        if (
                            game_map[y][x] == TILES["fire"]
                            and (y, x) not in fire_timers
                        ):
                            fire_timers[(y, x)] = FIRE_LIFETIME

        for (y, x), time_left in list(fire_timers.items()):
            fire_timers[(y, x)] -= 1
            if fire_timers[(y, x)] <= 0:
                game_map[y][x] = TILES["ground"]
                del fire_timers[(y, x)]

        if tick % WEATHER_UPDATE_TICKS == 0:
            generate_weather(game_map, weather_map)

        if current_key in ["w", "a", "s", "d"]:
            helicopter.move(current_key, game_map)
            current_key = None

        y, x = helicopter.y, helicopter.x

        if game_map[y][x] == TILES["water"] and water < water_capacity:
            water += 1

        if game_map[y][x] == TILES["fire"] and water > 0:
            game_map[y][x] = TILES["ground"]
            score += 1
            water -= 1
            if (y, x) in fire_timers:
                del fire_timers[(y, x)]

        if game_map[y][x] == TILES["shop"] and score >= 5:
            score -= 5
            water_capacity += 1

        if game_map[y][x] == TILES["hospital"] and score >= 3 and lives < 20:
            score -= 3
            lives += 1

        if (y, x) in weather_map and weather_map[(y, x)]["type"] == TILES["storm"]:
            if storm_cooldown == 0:
                lives -= 1
                storm_cooldown = 20

        if storm_cooldown > 0:
            storm_cooldown -= 1

        display_map = [row.copy() for row in game_map]

        for (wy, wx), info in list(weather_map.items()):
            display_map[wy][wx] = info["type"]
            info["timer"] -= 1
            if info["timer"] <= 0:
                del weather_map[(wy, wx)]

        helicopter.draw(display_map)

        tree_count = sum(1 for row in game_map for cell in row if cell == TILES["tree"])
        if tree_count == 0:
            print("🌲 Все деревья сгорели! GAME OVER.")
            break

        if lives <= 0:
            print("💀 Вертолёт разбился! GAME OVER.")
            break

        print_map(display_map, water, water_capacity, lives, score)

        if save_requested:
            game_data = {
                "game_map": game_map,
                "fire_timers": {f"{y},{x}": t for (y, x), t in fire_timers.items()},
                "weather_map": {f"{y},{x}": v for (y, x), v in weather_map.items()},
                "helicopter": [helicopter.y, helicopter.x],
                "water": water,
                "water_capacity": water_capacity,
                "lives": lives,
                "score": score,
                "tick": tick,
            }
            save_game(save_file, game_data)
            save_requested = False

        time.sleep(TICK_DELAY)
        tick += 1

    game_data = {
        "game_map": game_map,
        "fire_timers": {f"{y},{x}": t for (y, x), t in fire_timers.items()},
        "weather_map": {f"{y},{x}": v for (y, x), v in weather_map.items()},
        "helicopter": [helicopter.y, helicopter.x],
        "water": water,
        "water_capacity": water_capacity,
        "lives": lives,
        "score": score,
        "tick": tick,
    }
    save_game(save_file, game_data)


if __name__ == "__main__":
    main()
