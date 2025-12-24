import sys


def paper_neighbors(grid: list[list[str]], loc: tuple[int, int]) -> int:
    p = -1
    for i in range(loc[0] - 1, loc[0] + 2):
        for j in range(loc[1] - 1, loc[1] + 2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "@":
                p += 1
    return p


grid = [list(line.rstrip("\n")) for line in sys.stdin.readlines()]
a = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@" and paper_neighbors(grid, (i, j)) < 4:
            a += 1

print(a)
