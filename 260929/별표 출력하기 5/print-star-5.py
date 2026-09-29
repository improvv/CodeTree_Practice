n = int(input())
a=n

for i in range(n):
    for j in range(a):
        for x in range(a):
            print('*',end='')
        print(' ', end='')
    print()
    a-=1
    
