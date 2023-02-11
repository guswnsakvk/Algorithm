import itertools

def solution(orders, course):
    answer = []
    orders_sort = []
    menu = {}
    for i in orders:
        lst = list(i)
        lst.sort()
        orders_sort.append("".join(lst))
        
    # print(orders_sort)
    
    for i in orders_sort:
        for j in course:
            if len(i) < j:
                break
                
            lst = itertools.combinations(i, j)
            # print(list(lst))
            # print('---')
            for k in lst:
                key = "".join(k)
                if key in menu:
                    menu[key] += 1
                else:
                    menu[key] = 1
    
    
    menu = sorted(menu.items(), key=lambda x: (len(x[0]), x[1]))
    print(menu)
    
    return answer