def solution(citations):
  answer = []
  citations.sort()
  for i in range(len(citations) // 2, len(citations)):
      if len(citations[:i]) <= citations[i] and len(citations[i:]) >= citations[i]:
          answer.append(citations[i])
          
  return answer[-1]