def josephus_survivor(n,k):
    res = []
    items = [i for i in range(1,n+1)]
    i = 0
    while items:
            i = (i + k - 1) % len(items)
            res.append(items.pop(i))
    return res[-1]
