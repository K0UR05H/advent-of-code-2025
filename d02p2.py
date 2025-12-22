import sys
from textwrap import wrap


def next_invalid(n: int, w_size: int):
    ns = str(n)
    if len(ns) % w_size == 0:
        c = wrap(ns, w_size)
        if len(c) > 1:
            if all(i == c[0] for i in c):
                return n
            else:
                p = int((len(ns) // w_size) * c[0])
                if p > n:
                    return p

                t = str(int(c[0]) + 1)
                p = int((len(ns) // w_size) * t)
                return p
        else:
            return next_invalid(int("1" + ((w_size * 2) - 1) * "0"), w_size)

    return next_invalid(int("1" + len(ns) * "0"), w_size)


def next_invalid_id(n: int):
    return min(next_invalid(n, w) for w in range(1, len(str(n)) + 1))


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
