import itertools

def bananas(s) -> set:
    result = set()
    slen = len(s)
    word = "banana"

    if slen == 6 and s == word:
        result.add(s)
    elif len(s) > 6:
        
        indexes=list(itertools.combinations( range(slen), slen-6))
        for index in indexes:
            resultword=''
            i=0
            k=0
            for j in range(slen):
                if j == index[i]:
                    resultword+= "-"
                    i +=1
                    if i>= len(index):
                        i -= 1
                else:
                    resultword += word[k]
                    k +=1
                    if k>= len(word):
                        k -= 1
            flag = True
            for i in range(slen):
                if resultword[i] != "-" and resultword[i] != s[i]:
                    flag = False
            if flag:
                result.add(resultword) 
    return result



