n = input()
arr = ['L', 'E', 'B', 'R', 'O', 'S']

for i in range(len(arr)):
    if n == arr[i]:
        print(i)
        break
else:
    print('None')