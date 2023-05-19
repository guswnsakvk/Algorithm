def solution(key, lock):
    answer = True
    n = len(key)
    m = len(key[0])
    keys = []
    keys.append(key)
    
    result = [[0]* n for _ in range(m)]
    
    for k in range(3):
        result = [[0]* n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                result[j][n-i-1] = keys[k][i][j]
                
        keys.append(result)
            
    for i in keys:
        print(i)

    return answer