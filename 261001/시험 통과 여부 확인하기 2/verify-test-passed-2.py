n = int(input())
num=[]
for i in range(n):
    score = list(map(int, input().split()))
    num.append(score)

cnt = 0

for i in range(len(num)):
    sum=0
    avg=0
    for j in num[i]:
        sum+=j
    avg=sum//4
    if avg>=60:
        print('pass')
        cnt+=1
    else:
        print('fail')
print(cnt)
        
    
    
