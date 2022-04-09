def solution(board, moves):
    answer = 0
    layer = [0] * len(board)
    stack = []
    
    for i in range(len(board)):
        for j in range(len(board[0])-1,-1,-1):
            if board[j][i] == 0:
                break
            else:
                layer[i] += 1
                
    for i in moves:
        if layer[i-1] != 0:
            if stack == []:
                stack.append(board[i-1][(layer[i-1])])
            else:
                if board[i-1][(layer[i-1])] == stack[len(stack)-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i-1][(layer[i-1])])
        else:
            continue
    
    return answer