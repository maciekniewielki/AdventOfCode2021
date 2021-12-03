from Common import *


def solve1(data):
    gamma, epsilon = calc_gamma_epsilon(data)
    return int(gamma, 2) * int(epsilon, 2)


def solve2(data):
    oxygen = solve_oxygen(data)
    co2 = solve_co2(data)
    return oxygen * co2


def calc_gamma_epsilon(data):
    most_common = []
    for i in range(len(data[0])):
        most_common.append([])
        for l in data:
            most_common[i].append(l[i])

    gamma = "".join([mode_b(x) for x in most_common])
    epsilon = "".join(["0" if x == "1" else "1" for x in gamma])
    return gamma, epsilon


def mode_b(num):
    c_0 = num.count("0")
    c_1 = num.count("1")
    if c_1 >= c_0:
        return "1"
    return "0"


def solve_oxygen(data):
    return solve_common(data, least_common=False)


def solve_co2(data):
    return solve_common(data, least_common=True)


def solve_common(data, least_common):
    for i in range(len(data[0])):
        common = calc_gamma_epsilon(data)[least_common]
        data = [x for x in data if x[i] == common[i]]
        if len(data) == 1:
            break
    return int(data[0], 2)


# IO
a = input_as_lines("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
