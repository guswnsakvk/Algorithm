import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
jewel = []

for _ in range(n):
  gram, price = map(int, input().split())
  jewel.append((gram, price))
  
jewel.sort(key=lambda x:x[0])

answer = 0

h = []
for _ in range(k):
  heapq.heappush(h, int(input()))

for _ in range(k):
  bag = heapq.heappop(h)
  tmp_bag = 0
  tmp_value = 0

  for i in range(len(jewel)):
    gram, price = jewel[i]

    if bag < gram:
      break
    else:
      if tmp_value < price:
        tmp_value = price
        tmp_bag = gram

  answer += tmp_value
  if tmp_value:
    jewel.remove((tmp_bag, tmp_value))

print(answer)