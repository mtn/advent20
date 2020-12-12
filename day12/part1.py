
def ang_to(ang):
    if ang == 90:
        return -1, 0
    elif ang == 180:
        return 0, -1
    elif ang == 270:
        return 1, 0
    elif ang == 0:
        return 0, 1

x = 0
y = 0
ang = 90
dirx, diry = ang_to(ang)
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        cmd = line[0]
        n = int(line[1:])

        if cmd == "F":
            x += dirx * n
            y += diry * n
        elif cmd == "E":
            x -= n
        elif cmd == "W":
            x += n
        elif cmd == "S":
            y -= n
        elif cmd == "N":
            y += n
        elif cmd == "L":
            ang = (ang - n + 360) % 360
            dirx, diry = ang_to(ang)
        elif cmd == "R":
            ang = (ang + n + 360) % 360
            dirx, diry = ang_to(ang)

print(abs(x) + abs(y))
