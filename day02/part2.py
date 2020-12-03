valid = 0
with open("input.txt") as f:
    for line in f:
        counts, letter, pw = line.strip().split()
        low, high = counts.strip().split("-")
        low, high = int(low), int(high)
        letter = letter[0]

        lowis = pw[low-1] == letter
        highis = pw[high-1] == letter
        if (lowis or highis) and not (lowis and highis):
            valid += 1

print(valid)
