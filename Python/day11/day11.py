from Common import *


def solve1(data):
    s = 0
    for _ in range(100):
        s += step(data)
    return s


def step(data):
    flashed = set()
    for i, l in enumerate(data):
        for j, x in enumerate(l):
            data[i][j] += 1

    while True:
        flashed_this_time = False
        for i, l in enumerate(data):
            for j, x in enumerate(l):
                if x > 9 and (i, j) not in flashed:
                    flashed_this_time = True
                    flashed.add((i, j))
                    flash(i, j, data)

        if not flashed_this_time:
            break

    for i, j in flashed:
        data[i][j] = 0

    return len(flashed)


def flash(i, j, data):
    for x in range(-1, 2):
        for y in range(-1, 2):
            if valid_index(i+x, j+y, data):
                data[i+x][j+y] += 1


def valid_index(i, j, array):
    return 0 <= i < len(array) and 0 <= j < len(array[i])


def solve2(data):
    all_octopuses = sum(len(row) for row in data)
    for s in range(1, 100000):
        f = step(data)
        if f == all_octopuses:
            return s


# IO
a = input_as_lines("input.txt")
array2d = [[int(digit) for digit in line] for line in a]


# 1st
print(solve1(array2d))

# 2nd
print(solve2(array2d))
