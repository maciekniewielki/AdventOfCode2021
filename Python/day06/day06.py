from Common import *
from collections import defaultdict


def solve1(data):
    data = data[:]
    for _ in range(80):
        iterate(data)
    return len(data)


def iterate(data):
    for i in range(len(data)):
        if data[i] == 0:
            data[i] = 6
            data.append(8)
        else:
            data[i] -= 1


def generate_iteration_lookup(iterations):
    in_out_map = {}
    for case in range(9):
        in_out_map[case] = defaultdict(int)
        single = [case]
        for _ in range(iterations):
            iterate(single)
        for n in range(9):
            in_out_map[case][n] += single.count(n)
    return in_out_map


def solve2(data, batch_size, batches):
    in_out_map = generate_iteration_lookup(batch_size)
    current_total = {k: 0 for k in range(9)}
    for num in data:
        current_total[num] += 1
    for _ in range(batches):
        total_this_iteration = defaultdict(int)
        for num in current_total:
            for num_results in in_out_map[num]:
                total_this_iteration[num_results] += current_total[num] * \
                    in_out_map[num][num_results]
        current_total = dict(total_this_iteration)
    return sum(current_total[k] for k in current_total)


# IO
a = [int(x) for x in input_as_string("input.txt").split(",")]

# 1st
print(solve1(a))

# 2nd
print(solve2(a, 16, 16))
