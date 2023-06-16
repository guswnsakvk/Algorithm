from itertools import permutations

n = int(input())

now = " ".join(input().split())
prev = " ".join(map(str, range(1,n+1)))

if now == prev:
    print(-1)
else:
    for p in permutations(map(str, range(1, n+1)), n):
        tmp = " ".join(p)
        if now == tmp:
            print(prev)
            break
        prev = tmp