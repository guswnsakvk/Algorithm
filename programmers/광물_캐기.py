from itertools import permutations

def solution(picks, minerals):
    pickaxs = []
    answer = 1e9
    
    for i in range(3):
        for j in range(picks[i]):
            pickaxs.append(i)
    
    per_num = min(len(minerals) // 5 if len(minerals) % 5 == 0 else len(minerals) // 5 + 1, len(pickaxs))
    
    pickax = permutations(pickaxs, per_num)
    
    for pick in pickax:
        fatigue = 0
        cnt = 0
        l = 0
        for miner in minerals:
            try:
                if pick[l] == 0:
                    fatigue += 1
                    cnt += 1
                    if cnt == 5:
                        l += 1
                        cnt = 0
                elif pick[l] == 1:
                    if miner == "diamond":
                        fatigue += 5
                    else:
                        fatigue += 1
                    cnt += 1
                    if cnt == 5:
                        l += 1
                        cnt = 0
                else:
                    if miner == "diamond":
                        fatigue += 25
                    elif miner == "iron":
                        fatigue += 5
                    else:
                        fatigue += 1
                    cnt += 1
                    if cnt == 5:
                        l += 1
                        cnt = 0
            except:
                answer = min(answer, fatigue)
                break
            
        answer = min(answer, fatigue)
    
    return answer