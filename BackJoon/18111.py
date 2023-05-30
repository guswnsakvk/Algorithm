n, m, inven = map(int, input().split())
answer_time = 1e9
answer_target = 0
ground = []

for i in range(n):
  ground.append(list(map(int, input().split())))

for target in range(257):
  check = False
  time = 0
  tmp = inven

  for i in range(n):
    for j in range(m):
      now_ground = ground[i][j]

      if now_ground == target:
        continue

      if now_ground > target:
        num = now_ground - target

        if num < 0:
          check = True
          break
        else:
          tmp += num
          time += num * 2

      if now_ground < target:
        num = target - now_ground

        if num > tmp:
          check = True
          break
        else:
          tmp -= num
          time += num

    if check:
      break

  if not check:
    if answer_time > time:
      answer_time = time
      answer_target = target
    elif answer_time == time:
      answer_target = max(answer_target, target)

print('{0} {1}'.format(answer_time, answer_target))