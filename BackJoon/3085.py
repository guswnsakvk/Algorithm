import copy
import sys

def getAnswer(tmp, n, answer):
    for i in range(n):
        num_col = 1
        candy_col = tmp[i][0]
        #print(candy)

        num_row = 1
        candy_row = tmp[0][i]
        for j in range(1, n):
            if candy_col == tmp[i][j]:
                num_col += 1
                if num_col == n:
                    return num_col
                #print(num)
            else:
                candy_col == tmp[i][j]
                if num_col > answer:
                    #print(num)
                    answer = num_col
                num_col = 1

            if candy_row == tmp[j][i]:
                num_row += 1
                if num_row == n:
                    #print(num)
                    return num_row
            else:
                candy_row = tmp[j][i]
                if num_row > answer:
                  #print(num)
                  answer = num_row
                num_row = 1
            
            if j == n-1:
                if num_col > answer:
                    answer = num_col
                if num_row > answer:
                    answer = num_row
                
    return answer

input = sys.stdin.readline
n = int(input())

bomboni = []
answer = 1

for i in range(n):
    bomboni.append(list(input()))

for i in range(n):
    for j in range(n-1):
        a = bomboni[i][j]
        b = bomboni[i][j+1]

        c = bomboni[j][i]
        d = bomboni[j+1][i]

        tmp = copy.deepcopy(bomboni)

        tmp[i][j] = b
        tmp[i][j+1] = a

        answer = getAnswer(tmp, n, answer)

        tmp = copy.deepcopy(bomboni)

        tmp[j][i] = d
        tmp[j+1][i] = c

        answer = getAnswer(tmp, n, answer)

print(answer)