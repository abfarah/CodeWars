def decrypt(encrypted_text, n):
    if n <=0:
        return encrypted_text
        
    result = encrypted_text
    while n > 0:
        tempResult = ''
        temp1 = result[:int(len(encrypted_text)/2)]
        temp2 = result[int(len(encrypted_text)/2):]
        for i in range(0, len(temp1), 1):
            tempResult += temp2[i]
            tempResult += temp1[i]
        
        if len(result) %2 != 0:
            tempResult += temp2[-1]
            
        result = tempResult
        n -= 1
    return result


def encrypt(text, n):
    if n <= 0:
        return text
    
    result = text
    while n > 0:
        tempResult = ''
        for i in range(1, len(result), 2):
            tempResult += result[i]
        for i in range(0, len(result), 2):
            tempResult += result[i]
        result = tempResult
        n -= 1
    return result
