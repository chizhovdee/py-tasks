pets = {}

name = input("Кличка питомца: ")
species = input("Вид питомца: ")
age = int(input("Возраст питомца: "))
owner = input("Имя владельца: ")

pets[name] = {"Вид питомца": species, "Возраст питомца": age, "Имя владельца": owner}

last_digit = age % 10
last_two_digits = age % 100

if 11 <= last_two_digits <= 14:
    age_word = "лет"
elif last_digit == 1:
    age_word = "год"
elif 2 <= last_digit <= 4:
    age_word = "года"
else:
    age_word = "лет"

print(
    f'Это {pets[name]["Вид питомца"]} по кличке "{name}". Возраст питомца: {age} {age_word}. Имя владельца: {pets[name]["Имя владельца"]}'
)
