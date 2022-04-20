def solution(citations):
  citations.sort(reverse=True)
  for i, citation in enumerate(citations, start=1):
      if citation <= i:
          return citation
  return 0