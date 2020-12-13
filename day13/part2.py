

with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    earliest = int(lines[0])
    steps = list(map(int, lines[1].replace("x,", "0,").split(",")))

nonzero = len([i for i in steps if i != 0])
t = 0
step = 1
good = set()
lastprnt = 0
while True:
    for i, s in enumerate(steps):
        if s == 0:
            continue
        if (t + i) % s == 0 and s not in good:
            step *= s
            good.add(s)

    if len(good) == nonzero:
        print(t)
        break

    t += step

