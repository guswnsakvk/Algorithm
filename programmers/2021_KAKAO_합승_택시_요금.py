from collections import deque
import copy

def solution(n, s, a, b, fares):
    # global fees
    answer = 0
    graph = [[] for _ in range(n+1)]
    fees = {}
    
    for fare in fares:
        start, end, fee = fare
        graph[start].append(end)
        graph[end].append(start)
        fees[str(start) + str(end)] = fee
        fees[str(end) + str(start)] = fee
        
    print(graph)
    print(fees)   
    
    s_to_a = dfs(s, a, graph, fees, n)
    s_to_b = dfs(s, b, graph, fees, n)
    a_to_b = dfs(a, b, graph, fees, n)
    
    print(s_to_a)
    print(s_to_b)
    print(a_to_b)
    
    return answer

def dfs(start, end, graph, fees, n):
    # global fees
    queue = deque()
    # queue.append((start, 0))
    
    visited = [False for _ in range(n+1)]
    visited[start] = True
    
    for i in graph[start]:
        # print(i)
        queue.append((i, fees[str(start) + str(i)], [str(start) + str(i), str(i) + str(start)]))
        if not visited[i] and i != end:
            visited[i] = True
    min_path = 1e9
    # print(visited)
    # print(queue)
    
    while queue:
        x, num, tmp = queue.popleft()
        
        if x == end and min_path > num:
            min_path = num
            for i in tmp:
                fees[i] = 0
            continue
        
        for g in graph[x]:
            # print(g)
            loard = copy.deepcopy(tmp)
            # print(g)
            # if g == end:
            #     num += fees[str(x) + str(g)]
            #     print(fees[str(x) + str(g)])
            #     print(num)
                
            
            if not visited[g]:
                loard.append(str(x) + str(g))
                loard.append(str(g) + str(x))
                # print(fees[str(x) + str(g)])
                # print(num)
                if g != end:
                    visited[g] = True
                queue.append((g, num + fees[str(x) + str(g)], loard))
                # print(queue)
            # print('---')
    return min_path