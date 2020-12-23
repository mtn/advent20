from collections import deque
from itertools import islice

inp = "135468729"

c = deque(list(map(int,inp)))
ind = 0

for i in range(100):
    c.rotate(-ind-1)
    c1 = c.popleft()
    c2 = c.popleft()
    c3 = c.popleft()
    c.rotate(1)

    dest = c[0]-1
    lowest = min(c)
    while dest >= lowest:
        if dest in c:
            break
        dest -= 1
    if dest == lowest - 1:
        dest = max(islice(c, 1, len(c)))
    destind = c.index(dest)
    c.rotate(-destind-1)
    c.appendleft(c3)
    c.appendleft(c2)
    c.appendleft(c1)
    c.rotate(destind)

one_ind = c.index(1)
cc = list(c)
print("".join(list(map(str,cc[1:]))))
