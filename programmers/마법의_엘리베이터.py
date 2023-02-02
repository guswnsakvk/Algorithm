def solution(storey):
    answer = 0
    while storey != 0:
        num = storey % 10
        if num <= 5:
            answer += num
        else:
            answer += (10 - num)
            storey += (10 - num)
            
        storey = storey // 10
    return answer