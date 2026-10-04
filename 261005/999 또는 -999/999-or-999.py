nums = list(map(int, input().split()))
arr = []

for n in nums:
    if n == 999 or n == -999:
        break
    arr.append(n)

print(max(arr), min(arr))




