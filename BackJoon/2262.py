import heapq
import sys
input = sys.stdin.readline

n = int(input())
rank = list(map(int, input().split()))
rank_len = n
answer = 0

for _ in range(n-1):
  heap = []
  cnt = abs(rank[0] - rank[1])
  heapq.heappush(heap, max(rank[0], rank[1]) * -1)

  for i in range(1, rank_len-1):
    tmp = abs(rank[i] - rank[i+1])

    if cnt > tmp:
      heap.clear()
      cnt = tmp
      heapq.heappush(heap, max(rank[i], rank[i+1]) * -1)
    elif cnt == tmp:
      heapq.heappush(heap, max(rank[i], rank[i+1]) * -1)
    
  rank_len -= 1
  rank.remove(heapq.heappop(heap) * -1)
  answer += cnt

print(answer)