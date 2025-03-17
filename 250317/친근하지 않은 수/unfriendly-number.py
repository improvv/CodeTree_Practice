a = int(input())
t = 0

for i in range(a+1):
    if not (i%2==0 or i%3==0 or i%5==0):
        t+=1
    
print(t)