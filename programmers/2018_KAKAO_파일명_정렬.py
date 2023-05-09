import re

def solution(files):
    answer = []
    tmp = []
    p = re.compile('[0-9]+')
    
    for i, file in enumerate(files):
        result = p.search(file)
        try:
            num = result.group()
            if len(num) > 5:
                num = num[:5]

            a = file.split(num)
            a.insert(1, num)    
            a.append(i)
            tmp.append(tuple(a))
        except:
            tmp.append((file, '', '', i))
    
    tmp.sort(key = lambda x : (x[0].lower(), int(x[1]), x[3]))    
    
    for file in tmp:
        answer.append("".join(file[:3]))
    
    return answer