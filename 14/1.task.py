my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def print_list(index=0):
    if index < len(my_list):
        print(my_list[index])
        print_list(index + 1)
    else:
        print("Конец списка")


print_list()
