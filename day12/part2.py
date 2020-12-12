
x = 0
y = 0
wx = -10
wy = 1
with open("input.txt") as f:
    for line in f:
      cmd = line[0]
      n = int(line[1:])

      if cmd == "F":
        x += n * wx
        y += n * wy
      elif cmd == "E":
        wx -= n
      elif cmd == "W":
        wx += n
      elif cmd == "S":
        wy -= n
      elif cmd == "N":
        wy += n
      elif cmd == "L":
        for i in range(n // 90):
          wx, wy = (wy, -wx)
      elif cmd == "R":
        for i in range(n // 90):
          wx, wy = (-wy, wx)

print(abs(x) + abs(y))
