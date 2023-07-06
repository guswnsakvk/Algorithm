from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = deque(map(int, input().split()))

answer = 0
socket = []

while lst:
    num = lst.popleft()

    if len(socket) != n:
        if num not in socket:
          socket.append(num)
    else:
        if num in socket:
            continue
        
        remove_num = socket[0]
        place = "".join(map(str, lst)).find(str(remove_num))
        print(place)

        if place != -1:
          for i in range(1, n):              
              tmp_place = "".join(map(str, lst)).find(str(socket[i]))
              if tmp_place == -1:
                  remove_num = socket[i]
                  break

              if tmp_place > place:
                  place = tmp_place
                  remove_num = socket[i]

        print(remove_num)
        socket.remove(int(remove_num))
        socket.append(num)
        print(socket)
        print('---')
        answer += 1

print(answer)