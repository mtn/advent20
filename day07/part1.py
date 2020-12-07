from collections import defaultdict


g = defaultdict(list)
with open("input.txt") as f:
    for line in f:
        if "no" in line:
            continue
        l = line.strip().split()
        container = l[0] + " " + l[1]
        num_first = int(l[4])
        first = l[5] + " " + l[6]

        cont_ind = line.find("contain")
        line = line[cont_ind + len("contain "):]

        contained = line.split(",")
        for c in contained:
            splt = c.split()
            g[container].append(splt[1] + " " + splt[2])

can_contain = []
for node in g:
    if node == "shiny gold":
        continue

    visited = set()
    q = [node]
    while q:
        n = q.pop()
        if n in visited:
            continue
        else:
            if n in g:
                q.extend(g[n])
            visited.add(n)

    if "shiny gold" in visited:
        can_contain.append(node)

print(len(can_contain))
