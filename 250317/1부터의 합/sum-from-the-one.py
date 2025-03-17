n = int(input())
a = 0

for i in range(100):
    a+=i
    if(a>=n):
        break

print(i)