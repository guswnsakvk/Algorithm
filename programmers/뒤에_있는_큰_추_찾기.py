def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                answer[i] = numbers[j]
                break
                
    return answer