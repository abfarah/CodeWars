from collections import deque
def knight(p1, p2):
    h1 = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
    h2 = { 1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h'}
    s = set()
    start = [h1[p1[0]], int(p1[1])]
    target = [h1[p2[0]],int(p2[1])]
    que1 = deque()
    que1.append(start)
    count = 0
    directions = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
    while que1:
        que2 = deque()
        count += 1
        while que1:
            temp = que1.pop()
            s.add(str(temp))
            a,b = temp[0],temp[1]
            for x,y in directions:
                x1 = a + x
                y1 = b + y
                if x1 < 1 or y1 < 1 or x1 > 8 or y1 > 8:
                    continue
                if [x1,y1] == target:
                    return count
                if str([x1,y1]) not in s:
                    que2.appendleft([x1,y1])
        que1 = que2
    return 0
