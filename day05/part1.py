

maxid = 0
with open("input.txt") as f:
    for line in f:
        low = 0
        high = 127
        left = 0
        right = 7
        for letter in line.strip():
            if letter == "F":
                high -= (high - low + 1) // 2
            if letter == "B":
                low += (high - low + 1) // 2
            if letter == "L":
                right -= (right - left + 1) // 2
            if letter == "R":
                left += (right - left + 1) // 2

        id = high * 8 + left
        maxid = max(id, maxid)
print(maxid)
