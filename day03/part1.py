m = []
x = 0
with open("input.txt") as f:
    for line in f:
        m.append(line.strip())

count = 0 
for row in m:
    if row[x % len(m[0])] == "#":
        count += 1
    x += 3

print(count)
