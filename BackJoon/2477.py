k = int(input())

bulid = {1 : [], 2 : [], 3 : [], 4 : []}
start = 0
a = 0
width = 0
height = 0


for _ in range(6):
    direction, length = map(int, input().split())
    bulid[direction].append(length)
    if start == 0:
        start = direction
    if len(bulid[direction]) == 2 and a == 0 and start == direction:
        width = bulid[direction][0]
        a = direction
    elif len(bulid[direction]) == 2 and a == 0:
        width = length
        a = direction

max_width = sum(bulid[1])
max_height = sum(bulid[3])

for i in range(4):
    if len(bulid[i+1]) == 2 and a != i + 1:
        height = bulid[i+1][0]

print(max_width, max_height)
print(width, height)
print((max_width * max_height - width * height) * k)