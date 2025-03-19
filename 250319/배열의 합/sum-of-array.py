arr = [list(map(int,input().split())) for _ in range(4)]

for row in arr:
    total = 0
    for i in row:
        total += i
    print(total)