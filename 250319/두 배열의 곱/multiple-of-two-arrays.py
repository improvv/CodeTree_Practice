arr1 = [list(map(int,input().split())) for i in range(3) ]
input()
arr2 = [list(map(int,input().split())) for j in range(3) ]
arr3 = []

for i in range(3):
    row = []
    for j in range(3):
        row.append(arr1[i][j] * arr2[i][j])
    arr3.append(row)

for i in range(3):
    for j in range(3):
        print(arr3[i][j], end=' ')
    print()