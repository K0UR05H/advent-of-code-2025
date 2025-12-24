import sys


def max_jolt(bank: str):
    m = 0
    for i, a in enumerate(bank):
        for b in bank[i + 1 :]:
            m = max(m, int(a + b))
    return m


banks = sys.stdin.read().splitlines()

s = sum(max_jolt(b) for b in banks)
print(s)
