N = int(input())
length = 4 * (N - 1) + 1
stars = [[' ' for i in range(length)] for j in range((6 * (N - 1)) + 1)]

if N == 1:
  print('*')
else:
  stars[0] = ['*' for _ in range(length)]
  for i in range(len(stars)):
    stars[i][0] = "*"

print(stars)
for i in stars:
  print("".join(i))