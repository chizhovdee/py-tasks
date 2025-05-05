num = int(input("Введите пятизначное число: "))

units = num % 10
tens = (num // 10) % 10
hundreds = (num // 100) % 10
thousands = (num // 1000) % 10
ten_thousands = (num // 10000) % 10

power_result = tens**units
multiplied = power_result * hundreds
difference = ten_thousands - thousands

if difference == 0:
    print(
        "Ошибка: деление на ноль невозможно (разность десятков тысяч и тысяч равна 0)."
    )
else:
    result = multiplied / difference
    print("Результат:", result)
