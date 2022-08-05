def solution(answers):
    answer = []
    student_score = [0,0,0]
    student_num = [-1,-1,-1]
    student_1_pattern = [1,2,3,4,5]
    student_2_pattern = [2,1,2,3,2,4,2,5]
    student_3_pattern = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(1, len(answers)+1):
        if i % 6 == 0: 
            student_num[0] = 0
        else:
            student_num[0] += 1
            
        if i % 9 == 0: 
            student_num[1] = 0
        else:
            student_num[1] +=1
            
        if i % 11 == 0: 
            student_num[2] = 0
        else:
            student_num[2] +=1
        
        if(answers[i-1] == student_1_pattern[student_num[0]]): student_score[0] += 1
        if(answers[i-1] == student_2_pattern[student_num[1]]): student_score[1] += 1
        if(answers[i-1] == student_3_pattern[student_num[2]]): student_score[2] += 1
    
    max_score = max(student_score)
    
    for i in range(3):
        if student_score[i] == max_score:
            answer.append(i+1)
        
    return answer