arr=[]
for _ in range(4):
    arr.append(list(map(int, input().split())))

hap=0
for i in range(len(arr)):
    for j in range(i+1):
        hap=hap+arr[i][j]

print(hap)