k = int(input())

bulid = {1 : [], 2 : [], 3 : [], 4 : []}

for _ in range(6):
    direction, length = map(int, input().split())
    bulid[direction].append(length)

max_width = sum(bulid[1])
max_height = sum(bulid[3])
width = 0
height = 0

for i in range(4):
    if len(bulid[i+1]) == 2 and height == 0:
        height = bulid[i+1][0]
    elif len(bulid[i+1]) == 2:
        width = bulid[i+1][1]

print(max_width, max_height)
print(width, height)
print((max_width * max_height - width * height) * k)