import sys
input = sys.stdin.readline

n = int(input())
max_dp = [0, 0, 1, 7, 11, 71]
min_dp = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22, 20]

for i in range(6, 101):
    max_dp.append(max_dp[i - 2] * 10 + 1)

num = '20'
n = 0
place = 1
for i in range(11, 101):
    if '2' in num:
        if '0' in num:
            num = str(int(num) + (8 * 10 ** n))
            min_dp.append(int(num))
            n += 1
        else:
            num = num.replace('2', '6')
            min_dp.append(int(num))
            n = 0
    elif '6' in num:
        num = num.replace('6', '8')
        min_dp.append(int(num))
        num = '10' + '8' * place
        min_dp.append(int(num))
        place += 1
    elif '8' in num:
        if '0' in num:
            num = num.replace('0', '8')
            min_dp.append(int(num))
        else:
            num = '2' + '0' * place 
            min_dp.append(int(num))

for _ in range(n):
    cnt = int(input())
    print(min_dp[cnt], max_dp[cnt])