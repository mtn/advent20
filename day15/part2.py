
from itertools import count

inp = "15,12,0,14,3,1"
nums = list(map(int, inp.split(",")))

ls = {n:i for i,n in enumerate(nums)}

spoken = len(nums) - 1
while len(nums) < 30000000:
    cur = nums[-1]
    if cur not in ls:
        ls[cur] = len(nums) - 1
        nums.append(0)
    else:
        nums.append(len(nums) - 1 - ls[cur])
        ls[cur] = len(nums) - 2

print(nums[-1])


