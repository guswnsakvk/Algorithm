def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in range(len(lost)):
        if(lost[i] == 1):
            if reserve in 2:
                answer += 1
                reserve.remove(2)
                continue
        if(lost[i] == n):
            if reserve in (n-1):
                answer += 1
                reserve.remove(n-1)
                continue
        if lost[i]-1 in reserve:
            answer += 1
            reserve.remove(lost[i]-1)
            continue
        if lost[i]+1 in reserve:
            answer += 1
            reserve.remove(lost[i]+1)
            continue
    return answer