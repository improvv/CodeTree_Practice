n = int(input())
a = 0

for i in range(101):
    a+=i
    if(a>=n):
        break

print(i)