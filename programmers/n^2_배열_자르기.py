def solution(n, left, right):
    answer = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            answer.append(max(i, j))
    
    return answer[left:right+1]