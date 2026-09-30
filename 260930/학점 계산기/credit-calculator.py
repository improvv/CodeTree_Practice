n = int(input())
arr = list(map(float,input().split()))

av = round(sum(arr)/n,1)
print(av)

if av>=4.0:
    print('Perfect')
elif av>=3.0:
    print('Good')
else:
    print('Poor')