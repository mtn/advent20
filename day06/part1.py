

ans = 0
with open("input.txt") as f:
    for line in f.read().strip().split("\n\n"):
        letters = set()
        for l in line.split("\n"):
            for ll in l:
                letters.add(ll)
        ans += len(letters)
print(ans)
