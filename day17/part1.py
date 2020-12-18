from collections import defaultdict
from copy import deepcopy
from itertools import combinations, product

g = defaultdict(bool)
with open("input.txt") as f:
    for y, line in enumerate(f):
        line = line.strip()
        for x, c in enumerate(line):
            g[(x, y, 0)] = c == "#"

def pgrid(g, z):
    ks = [k for k in g.keys() if k[-1] == z]
    maxx = max(k[0] for k in ks)
    minx = min(k[0] for k in ks)
    maxy = max(k[1] for k in ks)
    miny = min(k[1] for k in ks)

    for y in range(miny, maxy+1):
        print("".join("#" if (x,y,z) in g and g[(x,y,z)] else "." for x in range(minx,maxx+1)))
    print()

def n(x,y,z):
    ns = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                if dx == dy == dz == 0:
                    continue
                ns.append((x+dx,y+dy,z+dz))
    return ns

for i in range(6):
    all_pts = set()
    for pt in g:
        all_pts.add(pt)
        all_pts.update(n(*pt))

    cpy = deepcopy(g)
    for x,y,z in all_pts:
        nn = sum(g[ne] for ne in n(x,y,z))
        if g[(x,y,z)] and nn not in [2,3]:
            cpy[(x,y,z)] = False
        elif not g[(x,y,z)] and nn == 3:
            cpy[(x,y,z)] = True
    g = cpy

print(sum(g.values()))
