def solution(m, musicinfos):
    answer = ''
    
    test = musicinfos[0]
    
    start, end, title, music = test.split(',')
    
    start_hour, start_minute = map(int, start.split(':'))
    print(start_hour, start_minute)
    
    end_hour, end_minute = map(int, end.split(':'))
    print(end_hour, end_minute)
    
    gap = (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)
    print(gap)
    
    repeat, rest = divmod(gap, len(music))
    music = music * repeat + music[:rest]
    print(music)
    
    if m in music:
        print(title)
    else:
        print("none")
        
    
    return answer