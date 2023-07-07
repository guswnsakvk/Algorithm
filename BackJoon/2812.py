n, k = map(int, input().split())

lst = list(map(int, input()))
stack = []

answer = []
count = 0
check = False
num = 0

for i in range(n):
  if k == 0:
    answer.append(lst[i])
  
  stack.append(lst[i])
  
  if stack and len(stack) == k+1 and k != 0:
    num = max(stack)
    check = True
  
  if check:
    for i in stack:
      if i == num:
        answer.append(num)
      else:
        k -= 1
    stack = []
    check = False

print("".join(map(str,answer)))