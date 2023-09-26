import sys
input = sys.stdin.readline

N, K, S = map(int, input().split())

answer = 0
cnt = 0
left = []
right = []

for _ in range(N):
    place, people = map(int, input().split())
    if S > place:
        left.append([place, people])
    else:
        right.append([place, people])

left.sort(reverse=True)
right.sort()

now = S

for idx, val in enumerate(left):
    answer += now - val[0]
    now = val[0]

    cnt += val[1]

    while cnt >= K:       
        if cnt == K and idx + 1 == len(left):
            break

        if idx + 1 != len(left):
            answer += (S - val[0]) * 2
            cnt -= K

if cnt:
    answer += S - left[-1][0]
cnt = 0
now = S

for idx, val in enumerate(right):
    answer += val[0] - now
    now = val[0]

    cnt += val[1]

    while cnt >= K:
        if cnt == K and idx + 1 == len(right):
            break

        if idx + 1 != len(right):
            answer += (val[0] - S) * 2
            cnt -= K

if cnt:
    answer += right[-1][0] - S

print(answer)