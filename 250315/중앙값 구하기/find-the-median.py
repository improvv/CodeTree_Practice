a, b, c = map(int, input().split())

if a>b:
    if b>c:
        print(b)
    elif a>c:
        print(c)
    else:
        print(a)
elif b<c:
    print(b)
else:
    print(c)