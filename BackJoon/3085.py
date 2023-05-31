import copy

def getAnswer(tmp, n, answer):
    for i in range(n):
        num = 1
        candy = tmp[i][0]
        #print(candy)
        for j in range(1, n):
            if candy == tmp[i][j]:
                num += 1
                if num == n:
                    return num
                #print(num)
            else:
                candy == tmp[i][j]
                if num > answer:
                    #print(num)
                    answer = num
                num = 1

            if j == n-1:
                if num > answer:
                    answer = num

    #print('---')

    for i in range(n):
        num = 1
        candy = tmp[0][i]
        #print(candy)
        for j in range(1, n):
            if candy == tmp[j][i]:
                num += 1
                if num == n:
                    #print(num)
                    return num
            else:
                candy = tmp[j][i]
                if num > answer:
                  #print(num)
                  answer = num
                num = 1
            
            if j == n-1:
                if num > answer:
                    answer = num

    #print(answer)
    #print('---')
            
    return answer

n = int(input())

bomboni = []
answer = 1

for i in range(n):
    bomboni.append(list(input()))


for i in range(n):
    for j in range(n-1):
        a = bomboni[i][j]
        b = bomboni[i][j+1]

        tmp = copy.deepcopy(bomboni)
        tmp[i][j] = b
        tmp[i][j+1] = a

        #for k in tmp:
        #    print(k)
        #print('---')
        answer = getAnswer(tmp, n, answer)
        #print(answer)
        #print('---')

        c = bomboni[j][i]
        d = bomboni[j+1][i]

        tmp = copy.deepcopy(bomboni)
        tmp[j][i] = d
        tmp[j+1][i] = c

        answer = getAnswer(tmp, n, answer)

print(answer)