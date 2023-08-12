import sys
input = sys.stdin.readline

n = int(input())
balloon = list(map(int, input().split()))
stack = []

for b in balloon:
  if not stack:
    stack.append(b-1)
    continue
  else:
    if b in stack:
      idx = stack.index(b)
      stack[idx] -= 1
    else:
      stack.append(b-1)

print(len(stack))