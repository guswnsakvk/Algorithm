import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int,input().split())) for _ in range(n)]

arr = []
for x, y in points:
    arr.append((x, 1))
    arr.append((y, -1))

arr.sort(key=lambda x: (x[0], x[1]))

cnt = 0
ans = 0
for x, v in arr:
    cnt += v
    ans = max(ans, cnt)

print(ans)