from Common import *
from statistics import mean, median


def solve1(data):
    middle = median(data)
    return calc_distance(lambda x, middle: abs(x - middle), middle, data)


def solve2(data):
    m = mean(data)
    correction = sum(1 if x > m else -1 for x in data) / (2 * len(data))
    middle = round(m + correction)
    return calc_distance(dist_sq, middle, data)


def dist_sq(target, source):
    diff = abs(target - source)
    return (diff * diff + diff) / 2


def calc_distance(dist_fun, middle_point, data):
    return int(sum(dist_fun(x, middle_point) for x in data))


# IO
a = [int(x) for x in input_as_string("input.txt").split(",")]

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
