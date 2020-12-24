from collections import defaultdict

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

print(sum(g.values()))
