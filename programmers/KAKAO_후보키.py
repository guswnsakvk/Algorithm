import copy

def solution(relation):
    unique = {'0': [],'1': [],'2': [],'3': [],'01': [],'02': [],'03': [],'12': [],'13': [],'23': [],'012': [],'013': [],'023': [],'123': [],'0123': []}
    
    for i in unique.keys():
        for j in relation:
            value = ''
            for k in range(len(i)):
                value += j[int(i[k])]
            if value not in unique[i]:
                unique[i].append(value)
                
                
    minimum = []
    check_len = len(relation)
    
    for key, value in unique.items():
        if len(value) == check_len:
            minimum.append(key)

    # print(minimum)
    answer = 0
    stack = []
    
#     for i in minimum:
#         flag = False
#         tmp = []
#         for j in i:
#             if j in stack:
#                 flag = True
#                 break
#             else:
#                 tmp.append(j)
    
#         if not flag:
#             stack.extend(tmp)
#             answer += 1
    
    for i in range(len(minimum)-1):
        for j in range(i+1, len(minimum)):
            if minimum[i] == '':
                continue
            
            for k in minimum[i]:
                if minimum[i] in minimum[j]:
                    minimum[j] = ''
            
    
    for i in minimum:
        if i != '':
            answer += 1
    
    return answer