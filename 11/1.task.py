def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


n = int(input())
start = factorial(n)

result_list = []
for i in range(n, 0, -1):
    result_list.append(factorial(i))

print(result_list)
