n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
arr=sorted(a, reverse=True)
print(arr[0], arr[1])

