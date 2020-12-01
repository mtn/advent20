entries = []
with open("input.txt") as f:
    for line in f:
        entries.append(int(line.strip()))

for i, e1 in enumerate(entries):
    for j, e2 in enumerate(entries):
        if i == j:
            continue
        if e1 + e2 == 2020:
            print(e1 * e2)
            exit()
