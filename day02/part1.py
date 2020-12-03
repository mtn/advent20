valid = 0
with open("input.txt") as f:
    for line in f:
        counts, letter, pw = line.strip().split()
        low, high = counts.strip().split("-")
        low, high = int(low), int(high)
        letter = letter[0]

        if low <= pw.count(letter) <= high:
            valid += 1

print(valid)
