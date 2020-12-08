from copy import deepcopy


with open("input.txt") as f:
    lines = f.read().strip().split("\n")


def run(lines):
    acc = 0
    ind = 0
    lines_run = set()
    while ind < len(lines):
        instr = lines[ind]
        cmd, arg = instr.strip().split()
        if ind in lines_run:
            return None
        lines_run.add(ind)
        if cmd == "nop":
            ind += 1
        elif cmd == "acc":
            if arg[0] == "-":
                acc -= int(arg[1:])
            else:
                acc += int(arg[1:])
            ind += 1
        else:
            if arg[0] == "-":
                ind -= int(arg[1:])
            else:
                ind += int(arg[1:])
    return acc


inds_to_replace = []
for i, l in enumerate(lines):
    if "nop" in l:
        inds_to_replace.append(i)
for i in inds_to_replace:
    llines = deepcopy(lines)
    llines[i] = llines[i].replace("nop", "jmp")

    acc = run(llines)
    if acc is not None:
        print(acc)
        exit()

inds_to_replace = []
for i, l in enumerate(lines):
    if "jmp" in l:
        inds_to_replace.append(i)
for i in inds_to_replace:
    llines = deepcopy(lines)
    llines[i] = llines[i].replace("jmp", "nop")

    acc = run(llines)
    if acc is not None:
        print(acc)
        exit()
