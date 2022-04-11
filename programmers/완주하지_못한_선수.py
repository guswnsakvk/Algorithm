def solution(participant, completion):
    for goal in completion:
        if goal in participant:
            participant.remove(goal)
    
    return participant[0]