from collections import deque

with open("input.txt") as f:
    players = f.read().strip().split("\n\n")

assert len(players) == 2

cards = {}
for i,p in enumerate(players):
    c = deque(map(int, p.split("\n")[1:]))
    cards[i] = c


while cards[0] and cards[1]:
    p1c = cards[0].popleft()
    p2c = cards[1].popleft()
    if p1c > p2c:
        cards[0].append(p1c)
        cards[0].append(p2c)
    else:
        cards[1].append(p2c)
        cards[1].append(p1c)

ans = 0
winner = list(cards[0]) or list(cards[1])
for i, c in enumerate(winner[::-1]):
    ans += (i+1) * c
print(ans)
