import sys
from functools import cache


@cache
def max_jolt(bank: str, l=11):
    if l == 0:
        return max(int(b) for b in bank)

    m = 0
    for i, a in enumerate(bank[:-l]):
        rm = max_jolt(bank[i + 1 :], l - 1)
        m = max(m, int(a + str(rm)))

    return m


banks = sys.stdin.read().splitlines()

s = sum(max_jolt(b) for b in banks)
print(s)
