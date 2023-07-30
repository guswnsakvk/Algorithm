A, P = map(int, input().split())

answer = [A]
idx = 0

while True:
    num = 0

    while A != 0:
        A, b = divmod(A, 10)
        num += b ** P

    if num not in answer:
        answer.append(num)
        A = num
    else:
        idx = answer.index(num)
        break

print(idx)
print(answer)