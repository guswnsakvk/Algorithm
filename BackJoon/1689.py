import sys
input = sys.stdin.readline

N = int(input())

answer = 1
tmp = 1

lines = []
for _ in range(N):
    lines.append(list(map(int, input().split())))

lines.sort(key=lambda x : -x[1])
start = lines[0][0]
end = lines[0][1]

for i in range(1, N):
    if start < lines[i][1]:
        tmp += 1
        start = max(start, lines[i][0])
    else:
        answer = max(answer, tmp)
        tmp = 1
        start = lines[i][0]
        end = lines[i][1]

print(max(answer, tmp))