def solution(citations):
  citations.sort()
  if len(citations) % 2 == 0:
      return citations[(len(citations) // 2) - 1]
  else:
      return citations[len(citations) // 2]