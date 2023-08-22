import sys
input = sys.stdin.readline

T = int(input())

lst = [(0,10),(10,20),(20,30),(30,40),(40,50),(50,60)]

for _ in range(T):
  N = int(input())
  ADDH = N // 60
  N %= 60

  idx = N // 10
  rest = N % 10
  left, right = lst[idx][0], lst[idx][1]
  left_answer = [0,0,0,0,0]
  right_answer = [0,0,0,0,0]

  if left > 30:
    left_answer[0] = 1
    left_answer[2] = 6 - idx
  else:
    left_answer[1] = idx

  if right > 30:
    right_answer[0] = 1
    right_answer[2] = 5 - idx
  else:
    right_answer[2] = idx + 1

  left_answer[3] = rest
  right_answer[4] = 10 - rest

  left_sum = sum(left_answer)
  right_sum = sum(right_answer)

  if left_sum < right_sum:
    left_answer[0] += ADDH
    print(*left_answer)
  elif left_sum > right_sum:
    right_answer[0] += ADDH
    print(*right_answer)
  else:
    if left_answer[0] < right_answer[0]:
      print(*left_answer)
      continue
    elif left_answer[0] > right_answer[0]:
      print(*right_answer)
      continue

    if left_answer[1] < right_answer[1]:
      print(*left_answer)
      continue
    elif left_answer[1] > right_answer[1]:
      print(*right_answer)
      continue

    if left_answer[2] < right_answer[2]:
      print(*left_answer)
      continue
    elif left_answer[2] > right_answer[2]:
      print(*right_answer)
      continue

    if left_answer[3] < right_answer[3]:
      print(*left_answer)
      continue
    elif left_answer[3] > right_answer[3]:
      print(*right_answer)
      continue

    if left_answer[4] < right_answer[4]:
      print(*left_answer)
      continue
    elif left_answer[4] > right_answer[4]:
      print(*right_answer)
      continue