def in_array(array1, array2):
    array1.sort()
    result = []
    for i in array1:
        for j in array2:
            if i in j and i not in result:
                result.append(i)
    return result
