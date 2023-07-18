import sys
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())

answer = 0
track = [0] * N
dates = []

for _ in range(M):
  send, take, box = map(int, input().split())
  dates.append((send, take, box))

dates.sort(key=lambda x:(-x[1], -x[0]))

for data in dates:
  send, take, box = data

  now_weight = sum(track[:take-1])

  if now_weight < C:
    now_weight += box
    if now_weight <= C:
      answer += box
      track[send-1] += box
      track[take-1] -= box
    else:
      num = box - (now_weight - C)
      now_weight -= num
      answer += num
      track[send-1] += num
      track[take-1] -= num

print(answer)