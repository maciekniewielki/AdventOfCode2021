from Common import *


def solve1(data):
    h = 0
    d = 0
    for l in data:
        command, amount = l.split(" ")
        amount = int(amount)
        if command == "forward":
            h += amount
        elif command == "down":
            d += amount
        elif command == "up":
            d -= amount
    return h * d


def solve2(data):
    h = 0
    d = 0
    a = 0
    for l in data:
        command, amount = l.split(" ")
        amount = int(amount)
        if command == "forward":
            h += amount
            d += amount * a
        elif command == "down":
            a += amount
        elif command == "up":
            a -= amount
    return h * d


# IO
a = input_as_lines("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
