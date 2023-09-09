import sys
input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
  lst.append(int(input()))

dp = [0] * (n)

for i in range(n-1, -1, -1):
  if i % 2:
    dp[i-1] = max(dp[i-1], dp[i] + lst[i])
    dp[i-2] = max(dp[i-2], dp[i] + lst[i])
  else:
    dp[i-2] += max(dp[i-1], dp[i] + lst[i])

print(max(dp[0] + 10, dp[1]))