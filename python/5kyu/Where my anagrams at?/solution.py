def anagrams(word, words):
    dict = {}
    result = []
    for i in word:
        if i not in dict:
            dict[i] = 1
        elif i in dict:
            dict[i] += 1
    
    for i in words:
        temp = {}
        if len(word) == len(i):
            for j in i:
                if j not in temp:
                    temp[j] = 1
                elif j in temp:
                    temp[j] +=1
        elif len(word) != len(i):
            continue
            
        if temp == dict:
            result.append(i)
    return result
