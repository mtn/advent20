
pub1 = 12232269
pub2 = 19452773

ls1 = None
ls2 = None
sn = 7
v = 1
i = 0
while True:
    v *= sn
    v %= 20201227
    i += 1

    if v == pub1:
        ls1 = i
    if v == pub2:
        ls2 = i

    if ls1 is not None and ls2 is not None:
        break

sn1 = pub1
v = 1
for i in range(ls2):
    v *= sn1
    v %= 20201227
print(v)


