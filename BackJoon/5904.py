N = int(input())
mo = "moo"
length = 2
n = 1

def game(mo, length, n):  
  if length >= N:
    print(mo[N-1])
    return

  mo = mo + "m" + ("o" * (n+2)) + mo
  length = length * 2 + n + 4
  n += 1
  game(mo, length, n)

game(mo, length, n)