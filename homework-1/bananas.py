import itertools
def name (k):
    print(k)
    

def bananas(s) -> set:
    result = set()
    key = ('b', 'a', 'n', 'a', 'n', 'a')
    comb=list(itertools.combinations( s, 6))
    indexes=list(itertools.combinations( range(len(s)) , 6))
    for i in range(len(comb)):
        if comb[i] == key:
            resultword = ''
            k=0
            l=0
            for j in range(len(s)):
                if j == indexes[i][l]:
                    resultword += key[k]
                    k += 1
                    l += 1
                    if l >= 6:
                        l -=1
                else:
                    resultword += '-'
            result.add(resultword)
    return  result
