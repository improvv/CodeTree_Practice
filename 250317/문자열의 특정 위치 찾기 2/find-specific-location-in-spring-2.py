arr = ['apple','banana','grape','blueberry','orange']
a = input()
c = 0

for i in arr:
    word=list(i)
    if word[3]==a or word[2]==a:
        print(i)
        c+=1

print(c)
