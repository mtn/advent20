
acc = 0
ind = 0
lines_run = set()
with open("input.txt") as f:
    lines = f.read().split("\n")
    while ind < len(lines):
        instr = lines[ind]
        cmd, arg = instr.strip().split()
        if ind in lines_run:
            break
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


print(acc)
