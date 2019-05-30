def first_non_repeating_letter(string):
    for i in string:
        counter = 0
        for j in string:
            if j.upper() == i or j.lower() == i or j == i:
                counter += 1
        if counter < 2:
            return i
    return ''
