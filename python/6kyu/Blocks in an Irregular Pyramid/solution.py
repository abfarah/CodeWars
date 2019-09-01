def blocks(w,l,h):
    h = h-1
    result = (((h * (h + 1) * ((2 * h) + 1))//6) + (((w+l) * h *(h+1))//2 + w * l * h) + w * l)
    return result
