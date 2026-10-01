n = list(map(int, input().split()))
even_sum=0
odd_sum=0
answer=0

for i in range(0,len(n),2):
    even_sum+=n[i]

for i in range(1,len(n),2):
    odd_sum+=n[i]

if even_sum>odd_sum:
    answer=even_sum-odd_sum
else:
    answer=odd_sum-even_sum

print(answer)