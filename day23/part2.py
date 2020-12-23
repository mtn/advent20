
from collections import deque
from itertools import islice

inp = "135468729"

class Node:
    def __init__(self, v, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

    def allafter(self):
        out = []
        n = self
        while True:
            if n.v in out:
                break
            out.append(n.v)
            n = n.r
        return " ".join(map(str, out))

    def __repr__(self):
        return str(self.v)


nodes = {}
last = None
for n in map(int,inp):
    nodes[n] = Node(n, l=last)
    if last:
        last.r = nodes[n]
    last = nodes[n]

for n in range(10, 1000001):
    nodes[n] = Node(n, l=last)
    last.r = nodes[n]
    last = nodes[n]

head = nodes[int(inp[0])]
tail = last
head.l = tail
tail.r = head


for i in range(10000000):
    card = head
    c1 = head.r
    c2 = c1.r
    c3 = c2.r
    head.r = c3.r

    nxt = card.v - 1
    while nxt in [c1.v, c2.v, c3.v]:
        nxt -= 1
    if nxt < 1:
        nxt = 1000000
        while nxt in [c1.v, c2.v, c3.v]:
            nxt -= 1

    dest = nodes[nxt]
    c3.r = dest.r
    dest.r.l = c3
    dest.r = c1
    c1.l = dest

    head = head.r

print(nodes[1].r.v*nodes[1].r.r.v)
