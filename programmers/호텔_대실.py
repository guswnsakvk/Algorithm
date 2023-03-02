def clean(hour, minute):
    if minute >= 60:
        hour += 1
        minute -= 60
    start = str(hour) + ":" + str(minute)
    return start

def solution(book_time):
    answer = 0
    stack = []
    book_time.sort(key = lambda x : (x[0], x[1]))
    for time in book_time:
        if not stack:
            stack.append(clean(int(time[1][:2]), int(time[1][3:]) + 10))
        else:
            flag = True
            for i in range(len(stack)):
                if stack[i] <= time[0]:
                    stack.pop(i)
                    stack.append(clean(int(time[1][:2]), int(time[1][3:]) + 10))
                    stack.sort()
                    flag = False
                    break
                    
            if flag:
                stack.append(clean(int(time[1][:2]), int(time[1][3:]) + 10))
            answer = max(answer, len(stack))
    return answer