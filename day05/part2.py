

seats = []
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
        seats.append(id)
seats.sort()

for s1, s2 in zip(seats, seats[1:]):
    if s2 != s1 + 1:
        print(s1+1)
        break
