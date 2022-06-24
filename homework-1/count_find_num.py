import itertools

def count_find_num(primesL, limit):
    result = 1
    maxpower = 0
    for i in primesL:
        result *= i
    if result == limit:
        return[1, result]
    while result*(primesL[0]**maxpower) < limit:
        maxpower += 1
    
    find_num=[]
    powers=set(itertools.combinations_with_replacement( range(1, maxpower+1), len(primesL)))
    for i in powers:
        power=set(itertools.permutations(i, len(primesL)))
        for j in power:
            
            result = 1
            for k in range(len(primesL)):
                result *= primesL[k]**j[k]
            if result <= limit:
                find_num.append(result) 
            
    if len(find_num) == 0:
            return []
    max_find_num = find_num[0]
    for i in find_num:
        if i > max_find_num:
            max_find_num = i
    return [len(find_num), max_find_num]

