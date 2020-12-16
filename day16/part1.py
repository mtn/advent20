
vf = {}
with open("input.txt") as f:
    sections = f.read().strip().split("\n\n")

for line in sections[0].split("\n"):
    splt = line.split()
    nind = line.index(":")
    name = line[:nind]

    valid = []
    rngs = line[nind+2:].split(" or ")
    for rng in rngs:
        low, high = map(int, rng.split("-"))
        valid.extend([i for i in range(low, high+1)])

    vf[name] = set(valid)

ans = 0
for n in sections[-1].split("\n")[1:]:
    nums = map(int, n.split(","))
    for nn in nums:
        good = False
        for v in vf.values():
            if nn in v:
                good = True
                break

        if not good:
            ans += nn

print(ans)






