n = int(input())
k = int(input())
answer = 0

gate = [False] * n
airplane_lst = []
for _ in range(k):
  airplane_lst.append(int(input()))

for airplane in airplane_lst:
  check = False
  
  for i in range(airplane-1, -1, -1):
    if not gate[i]:
      answer += 1
      gate[i] = True
      check = True
      break

  if not check:
    break

print(answer)