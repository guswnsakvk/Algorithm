from collections import deque
import copy

def solution(board):
    x_len = len(board)
    y_len = len(board[0])
    
    start = find_R(board, x_len, y_len)
    
    visited = [[False for j in range(y_len)] for i in range(x_len)]
    visited[start[0]][start[1]] = True
    
    answer = bfs(board, start, x_len, y_len, visited)

    return answer

def find_R(board, x_len, y_len):
    for i in range(x_len):
        for j in range(y_len):
            if board[i][j] == "R":
                return [i, j]
            
            
def bfs(board, start, x_len, y_len, visited):
    move = 1e9

    queue = deque()
    queue.append((start[0], start[1], 0, visited))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x, y, cnt, tmp = queue.popleft()
        
        for i in range(4):
            check = copy.deepcopy(tmp)
            
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= x_len or ny >= y_len:
                continue
                
            if board[nx][ny] == "D":
                continue
                
            while True:
                nx += dx[i]
                ny += dy[i]
                
                if nx < 0 or ny < 0 or nx >= x_len or ny >= y_len:
                    nx -= dx[i]
                    ny -= dy[i]
                    check[nx][ny] = True
                    print(nx, ny)
                    print(check)
                    
                    if board[nx][ny] == "G":
                        move = min(move, cnt+1)
                    else:
                        queue.append((nx, ny, cnt+1, check))
                    
                    break
                    
                if check[nx][ny] == True:
                    break
                    
                if board[nx][ny] == "D":
                    check[nx][ny] = True
                    nx -= dx[i]
                    ny -= dy[i]
                    print(nx, ny)
                    print(check)
            
                    if board[nx][ny] == "G":
                        move = min(move, cnt+1)
                    else:
                        queue.append((nx, ny, cnt+1, check))
                    
                    break
            
        print('---')
    print(visited)
    
    return move if move != 1e9 else -1