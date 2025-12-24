import sys


def paper_neighbors(grid: list[list[str]], loc: tuple[int, int]) -> int:
    p = -1
    for i in range(loc[0] - 1, loc[0] + 2):
        for j in range(loc[1] - 1, loc[1] + 2):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "@":
                p += 1
    return p


def can_be_removed(grid: list[list[str]], loc: tuple[int, int]) -> bool:
    if grid[loc[0]][loc[1]] == "@" and paper_neighbors(grid, loc) < 4:
        return True
    else:
        return False


def find_removable(grid: list[list[str]]) -> list[tuple[int, int]]:
    removable = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if can_be_removed(grid, (i, j)):
                removable.append((i, j))
    return removable


def remove(grid: list[list[str]], to_be_removed: list[tuple[int, int]]):
    for i, j in to_be_removed:
        grid[i][j] = "."


grid = [list(line.rstrip("\n")) for line in sys.stdin.readlines()]
a = 0
while removable := find_removable(grid):
    a += len(removable)
    remove(grid, removable)

print(a)
