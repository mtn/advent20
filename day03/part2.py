m = []
x = 0
with open("input.txt") as f:
    for line in f:
        m.append(line.strip())

acc = 1
ds = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for dx, dy in ds:
    x = 0
    y = 0

    count = 0
    while y < len(m):
        if m[y][x % len(m[0])] == "#":
            count += 1
        x += dx
        y += dy

    acc *= count

print(acc)
