
from collections import defaultdict

mem = defaultdict(int)
with open("input.txt") as f:
    for line in f:
        # line = "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
        splt = line.strip().split()
        if line.startswith("mask ="):
            mask = splt[-1]
        else:
            ind = int(splt[0][4:-1])
            num = int(splt[-1])
            # num = 11

            n = []
            for m in mask[::-1]:
                if m == "X":
                    n.append(str(num & 1))
                elif m == "0":
                    n.append("0")
                elif m == "1":
                    n.append("1")
                num = num >> 1

            n = n[::-1]
            val = int("".join(n), 2)
            mem[ind] = val
            # print(val)

tot = 0
for ind in mem:
    tot += mem[ind]
print(tot)



