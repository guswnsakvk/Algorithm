def solution(n, left, right):
    answer = []
    num = 0
    flag = False
    for i in range(1, n+1):
        for j in range(1, n+1):
            if num >= left and num <=right:
                answer.append(max(i, j))
            num += 1
            if num > right:
                flag = True
                break
        if flag:
            break

    return answer