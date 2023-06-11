from itertools import permutations
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

answer = 1e9
graph = []
house = []
chicken = []

for i in range(n):
  lst = list(map(int, input().split()))
  for j in range(n):
    if lst[j] == 1:
      house.append((i, j))

    if lst[j] == 2:
      chicken.append((i, j))

live_chicken = permutations(chicken, m)

for live in live_chicken:
  tmp = {}

  for h in house:
    tmp[str(h[0])+str(h[1])] = 1e9
  
  for l in live:
    for h in house:
      tmp[str(h[0])+str(h[1])] = min(tmp[str(h[0])+str(h[1])], abs(l[0] - h[0]) + abs(l[1] - h[1]))

  answer = min(answer, sum(tmp.values()))

print(answer)