## ([()(())](())([[]]()))()[()]
## 96

## (()[[]])([])
## 28

## ((((((()))))))
## 128

s = input()

stack = []
answer = 0
num = 0
tmp = 0
check = False

for index, i in enumerate(s):
    if stack:
        if i == '(' or i == '[':
            stack.append(i)
            if num != 0:
                tmp += num
                num = 0
                print(index)
                print(stack)
                print('num : ' + str(num))
                print('tmp : ' + str(tmp))
                print('---')
        else:
            if i == ')' and stack[-1] == '(':
                if len(stack) == 1:
                    if tmp == 0 and num == 0:
                        answer += 2
                    else:
                        num += tmp
                        num = num * 2
                        answer += num
                        num = 0
                        tmp = 0
                    print(index)
                    print(stack)
                    print('num : ' + str(num))
                    print('tmp : ' + str(tmp))
                    print('answer : ' + str(answer))
                    print('---')
                else:
                  if num != 0:
                      num *= 2
                  else:
                      num = 2
                  print(index)
                  print(stack)
                  print('num : ' + str(num))
                  print('tmp : ' + str(tmp))
                  print('answer : ' + str(answer))
                  print('---')
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                if len(stack) == 1:
                    if tmp == 0 and num == 0:
                        answer += 3
                    else:
                        num += tmp
                        num = num * 3
                        answer += num
                        num = 0
                        tmp = 0
                    print(index)
                    print(stack)
                    print('num : ' + str(num))
                    print('tmp : ' + str(tmp))
                    print('answer : ' + str(answer))
                    print('---')
                else:
                  if num != 0:
                      num *= 3
                  else:
                      num = 3
                  print(index)
                  print(stack)
                  print('num : ' + str(num))
                  print('tmp : ' + str(tmp))
                  print('answer : ' + str(answer))
                  print('---')
                stack.pop()
            else:
                check = True
                break
    else:
        if i == ')' or i == ']' or i == '{' or i == '}':
            check = True
            break
        else:
            stack.append(i)
            print(index)
            print(stack)
            print('---')

if stack or check:
    print(0)
else:
    print(answer)