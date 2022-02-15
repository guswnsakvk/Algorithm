t = int(input())

for _ in range(t):
  n = int(input())
  answer = n
  test = [True for _ in range(n)]
  case = []
  for i in range(n):
    lst = list(map(int, input().split()))
    case.append(lst)
  
  for i in range(n):
    for j in range(n):
      if(case[i][0] > case[j][0] and case[i][1] > case[j][1]):
        test[i] = False
        break

  for i in range(n):
    if(not test[i]):
      answer -= 1

  print(answer)