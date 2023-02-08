def solution(info, query):
    answer = []
    volunteers = []
    
    for i in info:
        lst = i.split()
        volunteers.append(lst)
    
    for requirement in query:
        requirement = requirement.replace(" and", "")
        lang, job, career, food, score = requirement.split(" ")
        num = 0
        for volunteer in volunteers:
            if lang != '-' and lang != volunteer[0]:
                continue
                
            if job != '-' and job != volunteer[1]:
                continue
                
            if career != '-' and career != volunteer[2]:
                continue
                
            if food != '-' and food != volunteer[3]:
                continue
                
            if score != '-' and int(score) > int(volunteer[4]):
                continue
                
            num += 1
            
        answer.append(num)
        
    return answer