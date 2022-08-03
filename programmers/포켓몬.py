def solution(nums):
    answer = 0
    poketmons = {}
    for poketmon in nums:
        if poketmon in poketmons:
            poketmons[poketmon] = +1
        else:
            poketmons[poketmon] = 1
    if(len(poketmons) >= len(nums) // 2):
        answer = len(nums) // 2
    else:
        answer = len(poketmons)
    return answer