with open("input.txt") as f:
    contents = f.read().strip()
    lines = contents.split("\n\n")

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
for line in lines:
    l = ",".join(line.split("\n")).replace(" ", ",").split(",")
    keys = []
    for ll in l:
        k, _ = ll.split(":")
        keys.append(k)
    all_in = True
    for f in fields:
        if f not in keys:
            all_in = False
    valid += all_in
print(valid)
