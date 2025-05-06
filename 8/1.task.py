n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    arr.append(num)

for i in range(n - 1, -1, -1):
    print(arr[i], end=" ")
