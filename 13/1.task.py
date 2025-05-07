import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matrix_1 = [[random.randint(-150, 150) for _ in range(cols)] for _ in range(rows)]
matrix_2 = [[random.randint(-150, 150) for _ in range(cols)] for _ in range(rows)]
matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range(cols)] for i in range(rows)]

print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nРезультат сложения (Матрица 3):")
for row in matrix_3:
    print(row)
