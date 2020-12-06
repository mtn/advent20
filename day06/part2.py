from collections import defaultdict


ans = 0
with open("input.txt") as f:
    for line in f.read().strip().split("\n\n"):
        lines = 0
        letters = defaultdict(int)
        for l in line.split("\n"):
            lines += 1
            for ll in set(l):
                letters[ll] += 1
        for ll, cnt in letters.items():
            if cnt == lines:
                ans += 1
print(ans)
