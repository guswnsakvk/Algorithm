def solution(targets):
    answer = 0
    targets.sort(key=lambda x:(x[1], x[0]))
    start = targets[0][0]
    end = targets[0][1]
    
    for i in range(1, len(targets)):
        if end <= targets[i][0]:
            answer += 1
            start = targets[i][0]
            end = targets[i][1]
        elif start <= targets[i][0] and end <= targets[i][1]:
            answer += 1
            start = targets[i][0]
            end = targets[i][1]
    
    return answer