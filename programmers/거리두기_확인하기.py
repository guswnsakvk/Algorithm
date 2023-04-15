def solution(places):
    answer = [1] * len(places)
    for cnt in range(len(places)):
        flag = False
        for i in range(5):
            for j in range(5):
                if places[cnt][i][j] == 'P':
                    if j - 1 > -1:
                        if places[cnt][i][j-1] == 'P':
                            flag = True
                            break
                        
                    if j + 1 < 5:
                        if places[cnt][i][j+1] == 'P':
                            flag = True
                            break
                            
                    if i - 1 > -1:
                        if places[cnt][i-1][j] == 'P':
                            flag = True
                            break
                    
                    if i + 1 < 5:
                        if places[cnt][i+1][j] == 'P':
                            flag = True
                            break
                    
                    if j - 2 > -1:
                        if places[cnt][i][j-2] == 'P' and places[cnt][i][j-1] == 'X':
                            continue
                        else:
                            flag = True
                            break
                        
                    if j + 2 < 5:
                        if places[cnt][i][j+2] == 'P' and places[cnt][i][j+1] == 'X':
                            continue
                        else:
                            flag = True
                            break
                        
                    if i - 2 > -1:
                        if places[cnt][i-2][j] == 'P' and places[cnt][i-1][j] == 'X':
                            continue
                        else:
                            flag = True
                            break
                            
                    if i + 2 < 5:
                        if places[cnt][i+2][j] == 'P' and places[cnt][i+1][j] == 'X':
                            continue
                        else:
                            flag = True
                            break
                            
                    if i - 1 > -1 and j - 1 > -1:
                        if places[cnt][i-1][j-1] == 'P' and (places[cnt][i][j-1] == 'X' or places[cnt][i-1][j] == 'X'):
                            continue
                        else:
                            flag = True
                            break
                            
                    if i - 1 > -1 and j + 1 < 5:
                        if places[cnt][i-1][j+1] == 'P' and (places[cnt][i][j+1] == 'X' or places[cnt][i-1][j] == 'X'):
                            continue
                        else:
                            flag = True
                            break
                            
                    if i + 1 > 5 and j - 1 < -1:
                        if places[cnt][i+1][j-1] == 'P' and (places[cnt][i][j-1] == 'X' or places[cnt][i+1][j] == 'X'):
                            continue
                        else:
                            flag = True
                            break
                            
                    if i + 1 > 5 and j + 1 < 5:
                        if places[cnt][i+1][j+1] == 'P' and (places[cnt][i][j+1] == 'X' or places[cnt][i+1][j] == 'X'):
                            continue
                        else:
                            flag = True
                            break
                        
            if flag:
                answer[cnt] = 0
                break

    return answer