def solution(s):
    answer = []
    s = s[1:-1]
    s = s.replace('{', '')
    s = s.replace("'",'')
    lst = s.split('},')
    lst[-1] = lst[-1][:-1]
    lst.sort(key=len)
    
    print(lst)
    
    for i in lst:
        num = ''
        for j in range(len(i)):
            if i[j] != ',':
                num += i[j]
                print(num)
            elif i[j] == ',' and int(num) not in answer:
                answer.append(int(num))
                num = ''
                break
            
            if len(i) - 1 == j and int(num) not in answer:
                answer.append(int(num))
                break
            # if j != ',' and int(j) not in answer:
            #     answer.append(int(j))
    
    return answer