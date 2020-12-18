
import re

def ev(exp):
    if "(" not in exp:
        nums = list(map(int, re.findall("-?\d+", exp)))
        ops = [c for c in exp if c in ["+", "*"]]
        if not ops:
            return nums[0]
        nnums = []
        acc = 0
        for i, op in enumerate(ops):
            if op == "+":
                acc += nums[i]
            elif op == "*":
                acc += nums[i]
                nnums.append(acc)
                acc = 0
        if ops[-1] == "*":
            nnums.append(nums[-1])
        else:
            nnums.append(acc + nums[-1])
        acc = 1
        for n in nnums:
            acc *= n
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
