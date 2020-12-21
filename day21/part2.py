from collections import defaultdict

allergin_possibilities = defaultdict(set)
ingredient_seen = defaultdict(set)
all_allergins = set()
with open("input.txt") as f:
    for j, line in enumerate(f):
        line = line.strip()
        if "(" in line:
            ind = line.index("(")
            ingredients = line[:ind]
            contains = line[ind:]
        else:
            ingredients = line
            constains = None

        ingredients = ingredients.strip().split()
        for i in ingredients:
            ingredient_seen[i].add(j)
        if contains is not None:
            allergins = contains[len("(contains "):-1].split(", ")

            all_allergins.update(allergins)
            for allergin in allergins:
                if allergin not in allergin_possibilities:
                    allergin_possibilities[allergin].update(ingredients)
                else:
                    allergin_possibilities[allergin] = allergin_possibilities[allergin].intersection(ingredients)


all_seen = set()
for k, v in allergin_possibilities.items():
    all_seen.update(v)

resolved = {}
while True:
    for allergin, ingredients in allergin_possibilities.items():
        if len(ingredients) == 1:
            ing = list(ingredients)[0]
            resolved[ing] = allergin
            for a, iss in allergin_possibilities.items():
                if ing in iss:
                    iss.remove(ing)
    done = True
    for al, ing in allergin_possibilities.items():
        if len(ing) > 0:
            done = False
            break

    if done:
        break

keys = list(resolved.items())
ks = [(x[1], x[0]) for x in keys]
ks.sort()
ks = [x[1] for x in ks]
print(",".join(ks))
