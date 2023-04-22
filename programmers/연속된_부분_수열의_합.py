def solution(sequence, k):
    seq_len = len(sequence)
    
    for i in range(1, seq_len+1):
        for j in range(seq_len):
            if j+i > seq_len:
                break
                
            cnt = sum(sequence[j:j+i])
            
            if cnt > k:
                break
            elif cnt == k:
                return [j,j+i-1]