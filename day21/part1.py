from collections import defaultdict

allergin_possibilities = defaultdict(set)
ingredient_seen = defaultdict(set)
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

            for allergin in allergins:
                if allergin not in allergin_possibilities:
                    allergin_possibilities[allergin].update(ingredients)
                else:
                    allergin_possibilities[allergin] = allergin_possibilities[allergin].intersection(ingredients)


all_seen = set()
for k, v in allergin_possibilities.items():
    all_seen.update(v)

ans = 0
for i in ingredient_seen:
    if i not in all_seen:
        ans += len(ingredient_seen[i])
print(ans)
