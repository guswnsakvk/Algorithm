N = int(input())
lst = [3, 4]
total = 0
num = 5
flag = False

if N == 0:
  print('m')
else:
  while True:
    for i in lst:
      total += i
      if total == N - 1:
        print('m')
        flag = True
        break
      elif total > N - 1:
        print('o')
        flag = True
        break

    if flag:
      break
    
    lst.insert(0, num)
    lst.insert(0, 3)
    num += 1