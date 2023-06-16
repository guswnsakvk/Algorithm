from itertools import permutations

n = int(input())

#now = tuple(input().split())
#prev = tuple(map(str, range(1,n+1)))

#if now == prev:
#    print(-1)
#else:
#    for p in permutations(map(str, range(1, n+1)), n):
#        if now == p:
#            print(" ".join(prev))
#            break
#        prev = p

for p in permutations(map(str, range(1, n+1)), n):
    print(p)