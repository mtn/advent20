from collections import defaultdict

possibilities = defaultdict(list)
with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    nums = list(map(int, lines))
    nums.sort()
    nums = [0] + nums + [max(nums)+3]

    options = [0] * len(nums)
    options[0] = 1

    for i in range(1, len(nums)):
        j = 0
        while 0 <= nums[i] - nums[i-j-1] <= 3:
            options[i] += options[i-j-1]
            j += 1

print(options[-1])
