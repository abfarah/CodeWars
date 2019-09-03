from collections import deque

def dirReduc(arr):
    s = deque()
    for i in arr:
        if len(s) == 0:
            s.append(i)
        else:
            j = s.pop()
            if i == "NORTH" and j != "SOUTH":
                s.append(j)
                s.append(i)
            elif i == "SOUTH" and j != "NORTH":
                s.append(j)
                s.append(i)
            elif i == "WEST" and j != "EAST":
                s.append(j)
                s.append(i)
            elif i == "EAST" and j != "WEST":
                s.append(j)
                s.append(i)
    if len(s) == 0:
        return []
    return list(s)
