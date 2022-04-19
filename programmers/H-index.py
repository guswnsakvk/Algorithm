def solution(citations):
  answer = 0
  avg = sum(citations) / len(citations)
  for citation in citations:
      if citation >= avg:
          answer += 1
  
  return answer