## 지원자들의 높은 점수대로 정렬하여
## for문을 돌릴 때 지원자의 점수가 요구하는 점수보다 낮을 경우 break

def solution(info, query):
    answer = []
    volunteers = []
    
    for i in info:
        lst = tuple(i.split())
        volunteers.append(lst)
    
    volunteers = sorted(volunteers, key = lambda x : int(x[4]), reverse = True )
    
    for requirement in query:
        requirement = requirement.replace(" and", "")
        lang, job, career, food, score = requirement.split(" ")
        n = 0
        for volunteer in volunteers:
            if score != '-' and int(score) > int(volunteer[4]):
                break
            
            if lang != '-' and lang != volunteer[0]:
                continue
                
            if job != '-' and job != volunteer[1]:
                continue
                
            if career != '-' and career != volunteer[2]:
                continue
                
            if food != '-' and food != volunteer[3]:
                continue
                
            n += 1
            
        answer.append(n)
        
    return answer