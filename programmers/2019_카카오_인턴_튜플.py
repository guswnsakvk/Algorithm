def solution(s):
    answer = []
    s = s[1:-1]
    s = s.replace('{', '')
    s = s.replace("'",'')
    lst = s.split('},')
    lst[-1] = lst[-1][:-1]
    lst.sort(key=len)
    
    for i in lst:
        print(i)
        for j in i:
            if j != ',' and int(j) not in answer:
                answer.append(int(j))
        
    
    return answer