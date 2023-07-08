n, k = map(int, input().split())

lst = list(map(int, input()))

stack = []
tmp = []
max_num = max(lst)
max_len = n-k

for i in range(n):  
  if k == 0:
    if len(tmp) <= max_len:
      tmp.append(lst[i])
    continue

  if lst[i] == max_num:
    while stack and k != 0:
        min_num = min(stack)
        stack.remove(min_num)
        k -= 1
    if i+1 >= n:
      max_num = max(lst[i:])
    else:
      max_num = max(lst[i+1:])
    tmp.extend(stack)
    tmp.append(lst[i])
    stack = []
  else:
    stack.append(lst[i])

print("".join(map(str, tmp[:max_len])))