from Common import *
from collections import defaultdict


def solve1(arr, alg):
    return count_in_iterations(arr, alg, 2)


def get_it_size(arr, it):
    lower_bound = min(arr.keys())
    upper_bound = max(arr.keys())
    return (lower_bound - it * 4, upper_bound + it * 4)


def count_in_iterations(arr, alg, it):
    it_size = get_it_size(arr, it)
    for i in range(it):
        arr = iterate(arr, alg, it_size)
    return count_light(arr, it, it_size)


def count_light(arr, it, window):
    count_window = window[0] + it, window[1] - it
    s = 0
    for line in range(count_window[0], count_window[1]):
        for col in range(count_window[0], count_window[1]):
            s += arr[line][col]
    return s


def iterate(arr, alg, it_size):
    out = defaultdict(lambda: defaultdict(int))
    for line in range(it_size[0], it_size[1]):
        for col in range(it_size[0], it_size[1]):
            out[line][col] = slide(line, col, arr, alg)
    return out


def slide(i, j, arr, alg):
    num = ""
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if arr[i+di][j+dj] == 1:
                num += "1"
            else:
                num += "0"
    num = int(num, 2)
    return alg[num]


def solve2(arr, alg):
    return count_in_iterations(arr, alg, 50)


# IO
a = input_as_string("input.txt")
parts = a.split("\n\n")
alg, rest = parts[0], parts[1:]

arr = defaultdict(lambda: defaultdict(int))
for i, line in enumerate(rest[0].split("\n")):
    for j, c in enumerate(line):
        if c == "#":
            arr[i][j] = 1
        else:
            arr[i][j] = 0

alg = [1 if x == "#" else 0 for x in alg]

# 1st
print(solve1(arr, alg))


# 2nd
print(solve2(arr, alg))
