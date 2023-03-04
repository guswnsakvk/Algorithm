n, m, start = map(int, input().split())

## 2차 배열 만들기
graph = [[] for _ in range(m)]
print(graph)
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

## dfs 방법으로 방문한 노드인지 표시하는 배열
dfs_visited = [False] * m
dfs_answer = []

## dfs 방법으로 노드 방문하는 함수
def dfs(graph, v, dfs_visited):
  ## 현재 노드는 방분했다고 True로 변경
  dfs_visited[v] = True
  dfs_answer.append(v)
  ## 현재 노드와 연결된 노드 중
  for i in graph[v]:
    ## 방문하지 않은 노드라면
    if not dfs_visited[i]:
      ## 방문
      dfs(graph, i, dfs_visited)

dfs(graph, start, dfs_visited)
print(dfs_answer)