def solution(numbers):
    new_numbers = []
    for i in range(len(numbers)):
        numbers_copy = numbers[1:].copy()
        for back in range(1, len(numbers)):
            new_numbers.append(str(numbers[0]) + "".join(map(str, numbers_copy)))
            numbers_copy.append(numbers_copy.pop(0))
        numbers.append(numbers.pop(0))
            
    return str(max(map(int, new_numbers)))