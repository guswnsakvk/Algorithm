n = int(input())
answer = "moo"
num = 1

while True:
  new = "moo" + ("o" * num) + "moo"
  answer += new
  num += 1
  if len(answer) > n:
    break

print(answer[n-1])