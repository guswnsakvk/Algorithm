def solution(sequence, k):
    answer = []
    cnt = 1e9
    seq_len = len(sequence)
    
    for i in range(seq_len):
        num = sequence[i]
        if num < k:
            for j in range(i+1, seq_len):
                num += sequence[j]
                if num > k:
                    break
                elif num == k and j - i < cnt:
                    cnt = j - i
                    answer = [i, j]
        elif num > k:
            break
        else:
            return [i, i]
    
    return answer