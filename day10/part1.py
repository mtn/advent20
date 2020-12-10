from collections import defaultdict

possibilities = defaultdict(list)
with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    nums = list(map(int, lines))
    nums.sort()

    one_diffs = 0
    three_diffs = 0

    for n1, n2 in zip(nums, nums[1:]):
        if n2 - n1 == 1:
            one_diffs += 1
        elif n2 - n1 == 3:
            three_diffs += 1

print((one_diffs + 1) * (three_diffs+1))
