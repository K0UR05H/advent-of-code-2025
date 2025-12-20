import sys


def moves_past_zero(s, v):
    if s and v:
        t = s + v
        if t <= 0 or t >= 100:
            return True
    return False


lines = sys.stdin.read().splitlines()

start = 50
zeros = 0
for rotation in lines:
    dir = rotation[0]
    v = int(rotation[1:])

    zeros += v // 100
    v %= 100
    v = v if dir == "R" else -v

    if moves_past_zero(start, v):
        zeros += 1

    start = (start + v) % 100

print(zeros)
