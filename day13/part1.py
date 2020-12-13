
with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    earliest = int(lines[0])
    steps = list(map(int, lines[1].replace("x,", "").split(",")))

t = earliest
while True:
    for s in steps:
        if t % s == 0:
            print(s * (t - earliest))
            exit()
    t += 1

