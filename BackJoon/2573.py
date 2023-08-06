from collections import deque
import copy
import sys
input = sys.stdin.readline

def bfs(i, j, visited):
    visited[i][j] = True

    queue = deque([(i, j)])

    while queue:
        x, y = queue.popleft()

        if x == 0 or x == N-1 or y == 0 or y == M-1:
           continue
        
        if ice[x][y] == 0:
           continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
               continue
            
            if visited[nx][ny]:
                continue
            
            visited[nx][ny] = True

            if ice[nx][ny] <= 0:
                tmp[x][y] -= 1
            else:
               queue.append((nx, ny))
               

N, M = map(int, input().split())

#ice = []
#for _ in range(N):
#    ice.append(list(map(int, input().split())))

ice = [
    [0,0,0,0,0],
    [0,0,9,0,0],
    [0,0,3,1,0],
    [0,0,9,0,0],
    [0,0,0,0,0]
]

tmp = copy.deepcopy(ice)

year = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

#cnt = 0

#visited = [[False for j in range(M)] for i in range(N)]

#for i in range(1, N-1):
#  for j in range(1, M-1):
#    if tmp[i][j] > 0 and not visited[i][j]:
#      cnt += 1
#      bfs(i, j, visited)

#for i in ice:
#   print(i)

#print('---')

#ice = copy.deepcopy(tmp)

#for i in ice:
#   print(i)

#print('---')


#for t in tmp:
#   print(t)

#print('---')

#print(cnt)

while True:
    visited = [[False for j in range(M)] for i in range(N)]
    cnt = 0

    for i in range(1, N-1):
        for j in range(1, M-1):
            if tmp[i][j] > 0 and not visited[i][j]:
                cnt += 1
                bfs(i, j, visited)

    if cnt >= 2:
        if year != 0:
            year += 1
        break
    elif cnt == 0:
        print(0)
        exit()
    else:
        year += 1

    ice = copy.deepcopy(tmp)

print(year)