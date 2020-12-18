
from collections import defaultdict
from copy import deepcopy
from itertools import combinations, product

g = defaultdict(bool)
with open("input.txt") as f:
    for y, line in enumerate(f):
        line = line.strip()
        for x, c in enumerate(line):
            g[(x, y, 0, 0)] = c == "#"

def n(x,y,z,w):
    ns = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(-1, 2):
                    if dx == dy == dz == dw == 0:
                        continue
                    ns.append((x+dx,y+dy,z+dz,w+dw))
    return ns

for i in range(6):
    all_pts = set()
    for pt in g:
        all_pts.add(pt)
        all_pts.update(n(*pt))

    cpy = deepcopy(g)
    for x,y,z,w in all_pts:
        nn = sum(g[ne] for ne in n(x,y,z,w))
        if g[(x,y,z,w)] and nn not in [2,3]:
            cpy[(x,y,z,w)] = False
        elif not g[(x,y,z)] and nn == 3:
            cpy[(x,y,z,w)] = True
    g = cpy

print(sum(g.values()))
