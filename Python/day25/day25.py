from Common import *
from collections import defaultdict


def solve1(map):
    iters = 1
    while iter(map):
        iters += 1
    return iters


def iter(map):
    positions_with_east = []
    for i in range(height):
        for j in range(wid):
            if map[i][j] == ">" and can_move(map, i, j, False):
                positions_with_east.append((i, j))

    for i, j in positions_with_east:
        map[i][j] = "."
        map[i][get_east(j)] = ">"

    positions_with_south = []
    for i in range(height):
        for j in range(wid):
            if map[i][j] == "v" and can_move(map, i, j, True):
                positions_with_south.append((i, j))

    for i, j in positions_with_south:
        map[i][j] = "."
        map[get_south(i)][j] = "v"

    return len(positions_with_east) + len(positions_with_south) > 0


def get_south(i):
    return (i+1) % height


def get_east(j):
    return (j+1) % wid


def can_move(map, i, j, south=True):
    if south:
        return map[get_south(i)][j] == "."
    else:
        return map[i][get_east(j)] == "."


# IO
map = defaultdict(lambda: defaultdict(lambda: "."))
a = input_as_lines("input.txt")
wid, height = len(a[0]), len(a)
for i, line in enumerate(a):
    for j, c in enumerate(line):
        map[i][j] = c


# 1st
print(solve1(map))
