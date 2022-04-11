def solution(participant, completion):
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            return i