import re

def ev(exp):
    if "(" not in exp:
        nums = list(map(int, re.findall("-?\d+", exp)))
        ops = [c for c in exp if c in ["+", "*"]]
        if not ops:
            return nums[0]
        acc = nums[0] * nums[1] if ops[0] == "*" else nums[0] + nums[1]
        for i, op in enumerate(ops[1:]):
            if op == "+":
                acc += nums[i+2]
            else:
                acc *= nums[i+2]
        return acc
    else:
        depth = 0
        for i, e in enumerate(exp):
            if e  == "(":
                if depth == 0:
                    start = i
                depth += 1
            elif e == ")":
                depth -= 1
                if depth == 0:
                    end = i
                    break
        exp = exp[:start] + str(ev(exp[start+1:end])) + exp[end+1:]
        return ev(exp)

ans = 0
with open("input.txt") as f:
    for line in f:
        ans += ev(line.strip())
print(ans)
