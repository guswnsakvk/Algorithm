n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    for j in range(1, len(arr[0])):
        arr[i][j] += arr[i][j-1]

for i in range(len(arr[0])):
    for j in range(1, len(arr)):
        arr[j][i] += arr[j-1][i]

k = int(input())

for i in arr:
    print(i)

for _ in range(k):
    answer = 0
    start_x, start_y, end_x, end_y = map(int, input().split())

    if start_x == end_x and start_y == end_y:
        if end_x == 1:
            if end_y == 1:
                print(arr[0][0])
            else:
              print(arr[end_x-1][end_y-1] - arr[end_x-1][end_y-2])
        else:
            if end_y == 1:
                print(arr[end_x-1][end_y-1] - arr[end_x-2][end_y-1])
            else:
                print(arr[end_x-1][end_y-1] - arr[end_x-1][end_y-2] - arr[end_x-2][end_y-1] + arr[end_x-2][end_y-2])
    elif start_x == 1 and start_y == 1:
        print(arr[end_x-1][end_y-1])
    else:
        if start_x == end_x:
            print(arr[end_x-1][end_y-1] - arr[end_x-2][end_y-1] - arr[end_x-1][start_y-2] + arr[end_x-2][start_y-2])
        else:
            print(arr[end_x-1][end_y-1] - arr[end_x-1][start_y-2])