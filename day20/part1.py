from collections import defaultdict
from itertools import combinations
import numpy as np
import re

with open("input.txt") as f:
    tiles = f.read().strip().split("\n\n")

tg = {}
for t in tiles:
    lines = t.strip().split("\n")
    id = int(re.findall("\d+", lines[0])[0])
    rows = []
    for y, row in enumerate(lines[1:]):
        rows.append(list(map(lambda x: x == "#", row)))

    m = np.array(rows)
    assert m.shape[0] == m.shape[1]
    tg[id] = m

def lrtb(m):
    l = m[:,0]
    r = m[:,-1]
    t = m[0,:]
    b = m[-1,:]
    return l,r,t,b

e2t = defaultdict(list)
for id, tile in tg.items():
    l,r,t,b = lrtb(tile)

    e2t[str(l)].append(id)
    e2t[str(r)].append(id)
    e2t[str(t)].append(id)
    e2t[str(b)].append(id)
    e2t[str(l[::-1])].append(id)
    e2t[str(r[::-1])].append(id)
    e2t[str(t[::-1])].append(id)
    e2t[str(b[::-1])].append(id)

possible = defaultdict(set)
for e, t in e2t.items():
    for t1 in t:
        for t2 in t:
            if t1 != t2:
                possible[t1].add(t2)
l = sorted(list(map(lambda x: (x[0], len(x[1])), possible.items())), key=lambda x: x[1])

ans = 1
for x,_ in l[:4]:
    ans *= x

print(ans)
