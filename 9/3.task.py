nums = list(map(int, input().split()))
seen = set()

for num in nums:
    if num in seen:
        print("YES")
    else:
        print("NO")
        seen.add(num)
