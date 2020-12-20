from collections import defaultdict, deque
from itertools import combinations
import numpy as np
import re

with open("input.txt") as f:
    tiles = f.read().strip().split("\n\n")
sl = int(len(tiles) ** 0.5)

tg = {}
for t in tiles:
    lines = t.strip().split("\n")
    id = int(re.findall("\d+", lines[0])[0])
    rows = []
    for y, row in enumerate(lines[1:]):
        rows.append(list(map(lambda x: x == "#", row)))

    m = np.array(rows)
    assert m.shape[0] == m.shape[1]
    orients = []
    for k in range(4):
        rot = np.rot90(m, k=k)
        orients.append(rot)
        orients.append(np.flipud(rot))

    for i, o in enumerate(orients):
        tg[(id,i)] = o

def lrtb(m):
    l = m[:,0]
    r = m[:,-1]
    t = m[0,:]
    b = m[-1,:]
    return l,r,t,b

tile = tg[list(tg.keys())[0]]
def g2s(g):
    outstrs = []
    for row in g:
        rowstr = "".join(list(map(lambda x: "#" if x else ".", row)))
        outstrs.append(rowstr)
    return "\n".join(outstrs)


monster = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""
mh = len(monster.split("\n")) - 1
mw = len(monster.split("\n")[0])
monster_coords = []
for y, row in enumerate(monster.split("\n")):
    for x, c in enumerate(row):
        if c == "#":
            monster_coords.append((y, x))
def search(pg):
    if len(pg) == len(tiles):
        placed_tids = set([x[0] for x in pg])
        assert len(placed_tids) == len(tiles)

        rows = []
        for row in range(sl):
            rows.append(np.hstack([tg[(id, oid)][1:-1,1:-1] for id,oid in pg[sl*row: sl*(row+1)]]))
        img = np.vstack(rows)

        orients = []
        for k in range(4):
            rot = np.rot90(img, k=k)
            orients.append(rot)
            orients.append(np.flipud(rot))

        for o in orients:
            used = set()
            for topy in range(len(o)-mh+1):
                for leftx in range(len(o[0])-mw+1):
                    if all([o[topy+my, leftx+mx] for my, mx in monster_coords]):
                        for my, mx in monster_coords:
                            used.add((topy+my, leftx+mx))

            if not used:
                continue
            else:
                print(np.sum(o) - len(used))
                exit()

        exit()

    row = len(pg) // sl
    col = len(pg) % sl
    placed_tids = [x[0] for x in pg]
    for (tid, oid), nt in tg.items():
        if tid in placed_tids:
            continue

        ml, mr, mt, mb = lrtb(nt)

        if row > 0:
            tabove = tg[pg[len(pg) - sl]]
            b = tabove[-1,:]
            if (b != mt).any():
                continue
        if col > 0:
            tleft = tg[pg[-1]]
            r = tleft[:,-1]
            if (r != ml).any():
                continue

        npg = list(pg)
        npg.append((tid, oid))
        search(npg)
search([])
