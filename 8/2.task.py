n = int(input())
a = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    if i == 0:
        result[i] = a[-1]
    else:
        result[i] = a[i - 1]

print(*result)
