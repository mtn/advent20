from collections import defaultdict
from copy import deepcopy

g = defaultdict(bool)
with open("input.txt") as f:
    for line in f:
        x = y = z = 0
        line = line.strip()
        i = 0
        while i < len(line):
            c1 = line[i]
            if i < len(line) - 1:
                c2 = line[i+1]
            else:
                c2 = None

            if c1 == "e":
                x += 1
                y -= 1
                i += 1
            elif c1 == "w":
                x -= 1
                y += 1
                i += 1
            elif c1+c2 == "se":
                y -= 1
                z += 1
                i += 2
            elif c1+c2 == "sw":
                x -= 1
                z += 1
                i += 2
            elif c1+c2 == "ne":
                x += 1
                z -= 1
                i += 2
            elif c1+c2 == "nw":
                z -= 1
                y += 1
                i += 2

        g[(x,y,z)] = not g[(x,y,z)]

ds = [(-1,1,0),(0,1,-1),(1,0,-1),(1,-1,0),(0,-1,1),(-1,0,1)]
for _ in range(100):
    gg = deepcopy(g)

    all_coords = set()
    for x,y,z in g.keys():
        if g[(x,y,z)]:
            all_coords.update([(x+dx,y+dy,z+dz) for dx,dy,dz in ds+[(0,0,0)]])

    for x,y,z in all_coords:
        neighbor_count = 0
        for dx,dy,dz in ds:
            if (x+dx,y+dy,z+dz) in g:
                neighbor_count += g[(x+dx,y+dy,z+dz)]
        white = not g[(x,y,z)] if (x,y,z) in g else True
        if not white:
            if neighbor_count == 0 or neighbor_count > 2:
                gg[(x,y,z)] = False
        else:
            if neighbor_count == 2:
                gg[(x,y,z)] = True

    g = gg

print(sum(g.values()))
