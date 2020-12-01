entries = []
with open("input.txt") as f:
    for line in f:
        entries.append(int(line.strip()))

for i, e1 in enumerate(entries):
    for j, e2 in enumerate(entries):
        for k, e3 in enumerate(entries):
            if i == j or i == k or j == k:
                continue
            if e1 + e2 + e3 == 2020:
                print(e1 * e2 * e3)
                exit()
