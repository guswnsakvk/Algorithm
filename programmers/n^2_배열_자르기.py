import copy

def solution(n, left, right):
    table = [[0 for i in range(n)] for j in range(n)]
    num = 1
    for i in range(n):
        for j in range(num):
            table[i][j] = i+1
            table[j][i] = i+1
        num += 1
    answer = []   
    for i in table:
        answer += copy.deepcopy(i)
    
    return answer[left:right+1]