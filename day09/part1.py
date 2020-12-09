
lines_run = set()
with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    nums = list(map(int, lines))

    ind = 25
    for i in range(ind, len(nums)):
        valid = False
        for j in range(i):
            for k in range(i):
                if j == k:
                    continue
                if nums[j] + nums[k] == nums[i]:
                    valid = True
                    break
            if valid:
                break
        if not valid:
            print(nums[i])
            break
