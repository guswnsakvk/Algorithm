from collections import deque

def solution(board):
    x_len = len(board)
    y_len = len(board[0])
    start = find_R(board, x_len, y_len)
    target = find_G(board, x_len, y_len)
    answer = bfs(board, start, target, x_len, y_len)
    print(start, target)
    return answer

def find_R(board, x_len, y_len):
    for i in range(x_len):
        for j in range(y_len):
            if board[i][j] == "R":
                return [i, j]
            
def find_G(board, x_len, y_len):
    for i in range(x_len):
        for j in range(y_len):
            if board[i][j] == "G":
                return [i, j]
            
def bfs(board, start, target, x_len, y_len):
    visited = [[False for j in range(y_len)] for i in range(x_len)]
    visited[start[0]][start[1]] = True
    
    move = 1e9

    queue = deque()
    queue.append((start[0], start[1], 0))
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    while queue:
        x, y, cnt = queue.popleft()
        
        print(x, y, cnt)
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= x_len or ny >= y_len:
                continue
                
            if board[nx][ny] == "D":
                continue
                
            if visited[nx][ny]:
                continue
                
            while True:
                visited[nx][ny] = True
                nx += dx[i]
                ny += dy[i]
                
                if nx < 0 or ny < 0 or nx >= x_len or ny >= y_len:
                    nx -= dx[i]
                    ny -= dy[i]
                    print(nx, ny)
                    
                    if board[nx][ny] == "G":
                        move = min(move, cnt+1)
                    else:
                        queue.append((nx, ny, cnt+1))
                    
                    break
                    
                if board[nx][ny] == "D":
                    nx -= dx[i]
                    ny -= dy[i]
                    print(nx, ny)
            
                    if board[nx][ny] == "G":
                        move = min(move, cnt+1)
                    else:
                        queue.append((nx, ny, cnt+1))
                    
                    break
            
        print('---')
    # print(visited)
    
    return move if move != 1e9 else -1