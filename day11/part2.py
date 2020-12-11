from copy import deepcopy

def follow_slp(grid, x, y, dx, dy):
    if dx == 0 and dy == 0:
        return "L"

    x += dx
    y += dy

    while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid) and grid[y][x] == ".":
        x += dx
        y += dy

    if not (x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid)):
        return "L"
    return grid[y][x]

def step(grid):
    cpy = deepcopy(grid)
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            full = 0

            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    full += follow_slp(grid, x, y, dx, dy) == "#"

            if grid[y][x] == "L" and not full:
                cpy[y][x] = "#"
            elif grid[y][x] == "#" and full >= 5:
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
