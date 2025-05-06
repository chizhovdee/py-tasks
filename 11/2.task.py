pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "Собака",
            "Возраст питомца": 9,
            "Имя владельца": "Павел",
        }
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 19,
            "Имя владельца": "Саша",
        }
    },
}


def get_pet(ID):
    return pets[ID] if ID in pets else False


def get_suffix(age):
    if 11 <= age % 100 <= 14:
        return "лет"
    elif age % 10 == 1:
        return "год"
    elif 2 <= age % 10 <= 4:
        return "года"
    else:
        return "лет"


def pets_list():
    for ID, info in pets.items():
        for name, data in info.items():
            suffix = get_suffix(data["Возраст питомца"])
            print(
                f'{ID}: Это {data["Вид питомца"]} по кличке "{name}". Возраст питомца: {data["Возраст питомца"]} {suffix}. Имя владельца: {data["Имя владельца"]}'
            )


def create():
    new_id = max(pets.keys()) + 1 if pets else 1
    name = input("Кличка питомца: ")
    species = input("Вид питомца: ")
    age = int(input("Возраст питомца: "))
    owner = input("Имя владельца: ")
    pets[new_id] = {
        name: {"Вид питомца": species, "Возраст питомца": age, "Имя владельца": owner}
    }
    print("Питомец добавлен.")


def read():
    ID = int(input("Введите ID питомца: "))
    pet = get_pet(ID)
    if pet:
        for name, data in pet.items():
            suffix = get_suffix(data["Возраст питомца"])
            print(
                f'Это {data["Вид питомца"]} по кличке "{name}". Возраст питомца: {data["Возраст питомца"]} {suffix}. Имя владельца: {data["Имя владельца"]}'
            )
    else:
        print("Питомец не найден.")


def update():
    ID = int(input("Введите ID питомца: "))
    pet = get_pet(ID)
    if not pet:
        print("Питомец не найден.")
        return
    for name in pet:
        new_name = input(f"Кличка ({name}): ") or name
        species = input("Вид питомца: ") or pet[name]["Вид питомца"]
        age = input("Возраст питомца: ")
        age = int(age) if age else pet[name]["Возраст питомца"]
        owner = input("Имя владельца: ") or pet[name]["Имя владельца"]
        pets[ID] = {
            new_name: {
                "Вид питомца": species,
                "Возраст питомца": age,
                "Имя владельца": owner,
            }
        }
        print("Информация обновлена.")
        break


def delete():
    ID = int(input("Введите ID питомца: "))
    if ID in pets:
        del pets[ID]
        print("Питомец удалён.")
    else:
        print("Питомец не найден.")


while True:
    command = (
        input("\nВведите команду (create/read/update/delete/list/stop): ")
        .strip()
        .lower()
    )
    if command == "stop":
        break
    elif command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    else:
        print("Неизвестная команда.")
