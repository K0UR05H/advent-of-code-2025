import sys


def next_invalid_id(n: int):
    ns = str(n)
    if len(ns) % 2 == 0:
        a, b = int(ns[: len(ns) // 2]), int(ns[len(ns) // 2 :])
        if b < a:
            return int(2 * str(a))
        elif a == b:
            return n
        else:
            return next_invalid_id(int(str(a + 1) + len(str(b)) * "0"))
    else:
        return int(2 * ("1" + (len(ns) // 2) * "0"))


inp = []
for r in sys.stdin.readline().split(","):
    a, b = map(int, r.split("-"))
    inp.append(range(a, b + 1))

invalid_sum = 0
for r in inp:
    start = r.start
    next = next_invalid_id(start)
    while next in r:
        invalid_sum += next
        next = next_invalid_id(next + 1)

print(invalid_sum)
