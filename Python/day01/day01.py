from Common import *

def solve1(data):
    return sum(y > x for x, y in zip(data, data[1:]))


def solve2(data):
    sums = [x+y+z for x,y,z in zip(data, data[1:], data[2:])]
    return solve1(sums)

# IO
a = input_as_ints("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
