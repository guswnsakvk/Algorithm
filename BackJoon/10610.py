from itertools import permutations

n = list(input())
n.sort(reverse=True)

len_n = len(n)
lst = permutations(n, len_n)

answer = 0

for l in lst:
    num = int("".join(l))
    
    if num % 30 == 0:
        answer = num
        break

if answer:
    print(answer)
else:
    print(-1)