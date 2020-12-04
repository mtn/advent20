
with open("input.txt") as f:
    contents = f.read().strip()
    lines = contents.split("\n\n")


fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
validcnt = 0
for line in lines:
    l = ",".join(line.split("\n")).replace(" ", ",").split(",")
    keys = []
    d = {}
    for ll in l:
        k, v = ll.split(":")
        d[k] = v

    valid = True
    for f in fields:
        if f not in d:
            valid = False
            break

    if not valid:
        continue

    if not d["byr"].isdigit() or not len(d["byr"]) == 4:
        valid = False
        continue
    elif not d["iyr"].isdigit() or not len(d["iyr"]) == 4:
        valid = False
        continue
    elif not d["eyr"].isdigit() or not len(d["eyr"]) == 4:
        valid = False
        continue

    byr = int(d["byr"])
    iyr = int(d["iyr"])
    eyr = int(d["eyr"])

    valid = valid and 1920 <= byr <= 2020
    valid = valid and 2010 <= iyr <= 2020
    valid = valid and 2020 <= eyr <= 2030

    if not valid:
        continue

    unit = d["hgt"][-2:]
    valid = valid and (unit == "cm" or unit == "in")
    if not valid:
        continue

    hgt = int(d["hgt"][:-2])
    if unit == "cm":
        valid = valid and 150 <= hgt <= 193
    else:
        valid = valid and 59 <= hgt <= 76

    hcl = d["hcl"]
    valid = valid and hcl[0] == "#"
    valid = valid and len(hcl) == 7
    for i in range(1, 7):
        valid = valid and (hcl[i].isdigit() or hcl[i].isalpha())

    valid = valid and d["ecl"] in ["amb", "blu", "brn","gry", "grn","hzl","oth"]
    valid = valid and d["pid"].isdigit() and len(d["pid"]) == 9

    validcnt += valid

print(validcnt)
