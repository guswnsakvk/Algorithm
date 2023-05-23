def solution(board, skill):
    answer = 0
    
    for kind, start_x, start_y, end_x, end_y, power in skill:
        for i in range(start_x, end_x + 1):
            for j in range(start_y, end_y + 1):
                if kind == 1:
                    board[i][j] -= power
                else:
                    board[i][j] += power
                    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    
    return answer