def solution(weights):
    answer = 0
    
    seesaw = []
    
    for weight in weights:
        seesaw.append([weight*2, weight*3, weight*4])
    
    for i in range(len(weights)-1):
        num1, num2, num3 = seesaw[i]
        for j in range(i+1, len(weights)):
            if num1 in seesaw[j] or num2 in seesaw[j] or num3 in seesaw[j]:
                answer += 1
    
    return answer
