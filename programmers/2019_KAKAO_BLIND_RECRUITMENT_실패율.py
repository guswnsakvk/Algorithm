def solution(N, stages):
  player = len(stages)
  dictionary = {key+1 : 0 for key in range(N)}
  for i in range(N):
      cnt = stages.count(i+1)
      dictionary[i+1] = cnt / player
      player -= cnt
  dictionary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
  return list(dictionary.keys())