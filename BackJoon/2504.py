s = input()

stack = []
answer = 0
num = 0
tmp = 0

for index, i in enumerate(s):
    if stack:
        if i == '(' or i == '[':
            stack.append(i)
            if num != 0:
                tmp += num
                num = 0
                print(index)
                print('num : ' + str(num))
                print('tmp : ' + str(tmp))
                print('---')
        else:
            if i == ')' and stack[-1] == '(':
                if len(stack) == 1:
                    if tmp == 0:
                        answer += 2
                    else:
                        num += tmp
                        num *= 2
                        answer += num
                        num = 0
                        tmp = 0
                    print(index)
                    print('num : ' + str(num))
                    print('tmp : ' + str(tmp))
                    print('---')
                else:
                  if num != 0:
                      num *= 2
                  else:
                      num = 2
                  print(index)
                  print('num : ' + str(num))
                  print('tmp : ' + str(tmp))
                  print('---')
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                if len(stack) == 1:
                    if tmp == 0:
                        answer += 3
                        num += tmp
                        num *= 3
                        answer += num
                        num = 0
                        tmp = 0
                    print(index)
                    print('num : ' + str(num))
                    print('tmp : ' + str(tmp))
                    print('---')
                else:
                  if num != 0:
                      num *= 3
                  else:
                      num = 3
                  print(index)
                  print('num : ' + str(num))
                  print('tmp : ' + str(tmp))
                  print('---')
                stack.pop()
            else:
                print(0)
                break
    else:
        if i == ')' or i == ']':
            print(0)
            break
        else:
            stack.append(i)

if stack:
    print(0)
else:
    print(answer)