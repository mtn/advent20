

ans = 29221323
lines_run = set()
with open("input.txt") as f:
    lines = f.read().strip().split("\n")
    nums = list(map(int, lines))

    for i in range(len(nums)):
        end = i+1
        r = nums[i:end]
        while sum(r) <= ans:
            if sum(r) == ans:
                if end == i+1:
                    continue
                print(min(r) + max(r))
                exit()
            end += 1
            r = nums[i:end]
