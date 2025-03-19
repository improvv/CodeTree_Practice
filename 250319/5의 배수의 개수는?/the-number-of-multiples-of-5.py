arr = [list(map(int, input().split())) for _ in range(4)]
cnt=0
for row in arr:
    for i in row:
        if i%5==0:
            cnt+=1

print(cnt)