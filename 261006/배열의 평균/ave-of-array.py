n = 2
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

for row in arr:
    print(f'{sum(row) / 4:.1f}', end=' ')
print()

for i in range(len(arr[0])):
    hap = arr[0][i] + arr[1][i]
    print(f'{hap / 2:.1f}', end=' ')
print()

hap2 = sum(arr[0], sum(arr[1]))
print(f'{hap2 / 8:.1f}')