from collections import deque

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

valid_inds = []
othertx = sections[-1].split("\n")[1:]
ans = 0
for i, n in enumerate(othertx):
    nums = map(int, n.split(","))
    valid_row = True
    for nn in nums:
        good = False
        for v in vf.values():
            if nn in v:
                good = True
                break

        if not good:
            ans += nn
            valid_row = False
    if valid_row:
        valid_inds.append(i)

possibilities = {k: set(i for i in range(len(vf.keys()))) for k in vf}
for i, n in enumerate(othertx):
    if i not in valid_inds:
        continue
    nums = list(map(int, n.split(",")))

    for ii, nn in enumerate(nums):
        for k, v in vf.items():
            if nn not in v and ii in possibilities[k]:
                possibilities[k].remove(ii)

determined = {}
p = list(possibilities.items())
p = sorted(p, key=lambda x: -len(x[1]))
while p:
    n, poss = p.pop()
    assert len(poss) == 1
    x = list(poss)[0]
    assert x not in determined.values()
    determined[n] = x

    for nm, posses in p:
        if x in posses:
            posses.remove(x)

    p = sorted(p, key=lambda x: -len(x[1]))

my = sections[1].split("\n")[1]
mynums = list(map(int, my.split(",")))

ans = 1
for k, ind in determined.items():
    if k.startswith("departure"):
        ans *= mynums[ind]
print(ans)
