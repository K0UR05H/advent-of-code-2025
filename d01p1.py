import sys

lines = sys.stdin.read().splitlines()
start = 50
zeros = 0
for rotation in lines:
    v = int(rotation[1:])
    if rotation[0] == "R":
        start += v
    else:
        start -= v
    start %= 100
    if start == 0:
        zeros += 1

print(zeros)
