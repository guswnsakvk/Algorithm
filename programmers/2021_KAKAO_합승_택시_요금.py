from collections import deque

def solution(n, s, a, b, fares):
    answer = 1e9
    graph = [[] for _ in range(n+1)]
    fees = {}
    
    for fare in fares:
        start, end, fee = fare
        graph[start].append(end)
        graph[end].append(start)
        fees[str(start) + str(end)] = fee
        fees[str(end) + str(start)] = fee
    
    for i in range(1, n+1):
        share = dfs(n, s, i, graph, fees)
        # print(share)
        
        if share[0] != 1e9:
            for j in share[1]:
                share_to_a = dfs(n, j, a, graph, fees)
                share_to_b = dfs(n, j, b, graph, fees)
                answer = min(answer, share[0] + share_to_a[0] + share_to_b[0])
            # print(share_to_a, share_to_b)
            # print('---')
    
    return answer

def dfs(n, s, e, graph, fees):
    path = 1e9
    tmp = []
    
    visited = [False for _ in range(n+1)]
    visited[s] = True
    
    queue = deque()
    queue.append((s, 0))
    
    while queue:
        x, num = queue.popleft()
        
        if x == e and path > num:
            path = num
            tmp.append(x)
            continue
        
        for g in graph[x]:
            if not visited[g]:
                visited[g] = True
                queue.append((g, num + fees[str(x) + str(g)]))
    
    return path, tmp