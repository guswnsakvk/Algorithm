from itertools import permutations
import copy

n = int(input())
words = []

for i in range(n):
  words.append(input())

## 입력된 알파벳 갯수를 구할 때 사용할 리스트
alphabet = set()
for word in words:
  for i in word:
    alphabet.add(i)

alphabet = list(alphabet)
## 단어를 숫자로 바꿀 때 사용할 숫자들을 저장하는 리스트
## ex) 입력 : 'AAA', 'BBB' -> ["9", "8"]
numbers = []
## {A:9, B:8} 이런씩으로 저장할 딕셔너리
dic = {}

for i in range(len(alphabet)):
  dic[alphabet[i]] = 0
  numbers.append(str(9-i))

answer = 0

## 모든 경우의 수를 구하기
for comb in permutations(numbers, len(numbers)):
  ## 딕셔너리에 값 초기화
  for i in range(len(dic)):
    dic[alphabet[i]] = comb[i]

  change_words = copy.deepcopy(words)
  ## 입력받은 문자열 숫자로 변경
  for i in range(len(change_words)):
    for key, value in dic.items():
      change_words[i] = change_words[i].replace(key, value)

  ## 변경된 문자열의 합을 answer보다 크면 answer에 저장
  answer = max(answer, sum(map(int, change_words)))

print(answer)