a, b = map(int, input().split())

while a<=b:
    print(a,end=' ')
    if a%2==0:
        a+=3
        if a>b:
            break
    else:
        a*=2
        if a>b:
            break