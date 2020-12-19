import re

with open("input.txt") as f:
    sections = f.read().strip().split("\n\n")

rules = sections[0].strip().split("\n")
examples = sections[1].strip().split("\n")

rls = {}
for r in rules:
    rid, rule = r.split(": ")
    rls[int(rid)] = rule

def flatten(rls, ind):
    rule = rls[ind]

    if rule.startswith('"'):
        return rule.replace('"', "")

    flattened_alts = []
    for a in rule.split(" | "):
        apts = []
        for aa in a.split(" "):
            apts.append(flatten(rls, int(aa)))
        flattened_alts.append("".join(apts))
    flattened_alts = "|".join(flattened_alts)

    return "(" + flattened_alts + ")"

ans = 0
f = flatten(rls, 0)
for e in examples:
    ans += re.fullmatch(f, e) is not None
print(ans)
