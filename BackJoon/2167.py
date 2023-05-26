n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

k = int(input())

for _ in range(k):
    answer = 0
    start_x, start_y, end_x, end_y = map(int, input().split())

    for i in range(start_x-1, end_x):
        for j in range(start_y-1, end_y):
            answer += arr[i][j]

    print(answer)