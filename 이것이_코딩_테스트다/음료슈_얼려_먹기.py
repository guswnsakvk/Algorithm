n, m= map(int, input().split())

## 이중배열만들기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

## dfs로 특정 노드 방문 후 연결된 노드 방문
def dfs(x,y):
  ## 값이 주어진 범위를 넘으면 멈추기
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False

  ## 현재 노드를 방문하지 않았으면
  if graph[x][y] == 0:
    ## 해당 노드 방문 처리
    graph[x][y] = 1
    ## 상, 하, 좌, 우 노드 방문
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

answer = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      answer += 1

print(answer)