a = int(input())
t = 0

for i in range(a):
    if i%2==0 or i%3==0 or i%5==0:
        t+=1
print(a-t)