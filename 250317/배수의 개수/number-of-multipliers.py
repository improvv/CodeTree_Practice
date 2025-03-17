c3=0
c5=0

for i in range(10):
    i=int(input())
    if i%3==0:
        c3+=1
        if i%5==0:
            c5+=1
    elif i%5==0:
        c5+=1

print(c3,c5,sep=' ')