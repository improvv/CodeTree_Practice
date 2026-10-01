n = list(map(int,input().split()))

sum = 0
cnt = 0

for i in n:
    if i==0:
        break
    else:
        sum+=i
        cnt+=1

print(f'{sum} {sum/cnt:.1f}')