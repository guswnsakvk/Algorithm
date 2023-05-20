def solution(n, build_frame):
    build = []
    tear_down = []
    
    for plan in build_frame:
        x, y, a, b = plan
        if b == 1:
            build.append([x, y, a])
        else:
            tear_down.append([x, y, a])
            
    print(build)
    print(tear_down)
        
    return []