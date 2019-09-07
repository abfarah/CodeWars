def josephus(items,k):
    res = []
    i = 0
    while items:
            i = (i + k - 1) % len(items)
            res.append(items.pop(i))
    return res
