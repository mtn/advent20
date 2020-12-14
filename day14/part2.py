from collections import defaultdict
from itertools import product

mem = defaultdict(int)
with open("input.txt") as f:
    for line in f:
        splt = line.strip().split()
        if line.startswith("mask ="):
            mask = splt[-1]
        else:
            ind = int(splt[0][4:-1])
            num = int(splt[-1])

            n = []
            floating = []
            for i, m in enumerate(mask[::-1]):
                if m == "X":
                    n.append("X")
                    floating.append(i)
                elif m == "0":
                    n.append(str(ind & 1))
                elif m == "1":
                    n.append("1")
                ind = ind >> 1

            n = n[::-1]
            for bs in product((0, 1), repeat=len(floating)):
                nn = list(n)
                for i, bv in zip(floating, bs):
                    nn[len(nn) - i - 1] = str(bv)
                ind = int("".join(nn), 2)
                mem[ind] = num


tot = 0
for ind in mem:
    tot += mem[ind]
print(tot)



