
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
            g[container].append((int(splt[0]), splt[1] + " " + splt[2]))

def get_count(key):
    tot = 1
    for cnt, node in g[key]:
        tot += cnt * get_count(node)

    return tot

print(get_count("shiny gold") - 1)
