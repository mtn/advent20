from collections import deque
from itertools import islice
from copy import deepcopy

with open("input.txt") as f:
    players = f.read().strip().split("\n\n")

assert len(players) == 2

seen = set()

cards = {}
for i,p in enumerate(players):
    c = deque(map(int, p.split("\n")[1:]))
    cards[i] = c


def step(p1c, p2c):
    p1card = p1c.popleft()
    p2card = p2c.popleft()

    if len(p1c) >= p1card and len(p2c) >= p2card:
        p1sub = deque(islice(p1c, 0, p1card))
        p2sub = deque(islice(p2c, 0, p2card))

        if rc(p1sub, p2sub) == 1:
            p1c.append(p1card)
            p1c.append(p2card)
        else:
            p2c.append(p2card)
            p2c.append(p1card)
    elif p1card > p2card:
        p1c.append(p1card)
        p1c.append(p2card)
    else:
        p2c.append(p2card)
        p2c.append(p1card)

def rc(p1c, p2c):
    seen = set()

    while p1c and p2c:
        h = (tuple(p1c), tuple(p2c))
        if h in seen:
            return 1
        seen.add(h)

        step(p1c, p2c)

    return 1 if p1c else 2

ans = 0
winner_ind = rc(cards[0], cards[1]) - 1
for i,c in enumerate(list(cards[winner_ind])[::-1]):
    ans += (i+1) * c
print(ans)
