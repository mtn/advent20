from copy import deepcopy

def step(grid):
    cpy = deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            full = 0
            empty = 0
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0 or x + dx < 0 or x + dx >= len(grid[0]) or y + dy < 0 or y + dy >= len(grid):
                        continue
                    if grid[y+dy][x + dx] == "L":
                        empty += 1
                    elif grid[y+dy][x + dx] == "#":
                        full += 1
            if grid[y][x] == "L" and not full:
                cpy[y][x] = "#"
            elif grid[y][x] == "#" and full >= 4:
                cpy[y][x] = "L"

    return cpy

grid = []
with open("input.txt") as f:
    for line in f:
        grid.append(list(line.strip()))

    while True:
        ngrid = step(grid)
        changed = False
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                changed = changed or grid[y][x] != ngrid[y][x]
        if not changed:
            break
        grid = ngrid

ans = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        ans += grid[y][x] == "#"
print(ans)

