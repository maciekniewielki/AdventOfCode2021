from Common import *


def solve1(data):
    s = 0
    for i, j in basins(data):
        s += data[i][j] + 1
    return s


def basins(data):
    b = []
    for i, l in enumerate(data):
        for j, x in enumerate(l):
            if not find_smaller_neighbour(i, j, data) and data[i][j] != 9:
                b.append((i, j))
    return b


def find_smaller_neighbour(i, j, arr):
    indexes = None
    if valid_index(i, j+1, arr) and arr[i][j+1] < arr[i][j]:
        indexes = i, j+1
    if valid_index(i, j-1, arr) and arr[i][j-1] < arr[i][j]:
        indexes = i, j-1
    if valid_index(i+1, j, arr) and arr[i+1][j] < arr[i][j]:
        indexes = i+1, j
    if valid_index(i-1, j, arr) and arr[i-1][j] < arr[i][j]:
        indexes = i-1, j

    return indexes


def valid_index(i, j, array):
    return 0 <= i < len(array) and 0 <= j < len(array[i])


def solve2(data):
    b = {k: 0 for k in basins(data)}
    for i, l in enumerate(data):
        for j, x in enumerate(l):
            if x == 9:
                continue
            indexes = descend_to_basin(i, j, data)
            b[indexes] += 1
    m = 1
    highest_vals = sorted([b[k] for k in b])[-3:]
    for k in highest_vals:
        m *= k
    return m


def descend_to_basin(i, j, arr):
    while True:
        indexes = find_smaller_neighbour(i, j, arr)
        if not indexes:
            return i, j
        i, j = indexes


# IO
a = input_as_lines("input.txt")
array2d = [[int(digit) for digit in line] for line in a]

# 1st
print(solve1(array2d))

# 2nd
print(solve2(array2d))
