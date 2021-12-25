from Common import *


def solve1(data):
    return find_num_with_generator(data, get_highest)


def find_num_with_generator(data, gen):
    var1, var2 = get_vars(data)
    relations = get_relations(var1, var2)
    num_vals = {}
    for i, j, const in relations:
        i_val, j_val = gen(const)
        num_vals[i] = i_val
        num_vals[j] = j_val

    final_num = ['0'] * 14
    for num_pos in num_vals:
        final_num[num_pos] = str(num_vals[num_pos])
    return "".join(final_num)


def get_vars(data):
    chunk_nums = []
    for i, line in enumerate(data):
        if "inp" in line:
            chunk_nums += [i]
    chunk_nums += [len(data)]
    chunks = []
    for start, end in zip(chunk_nums, chunk_nums[1:]):
        chunks.append(data[start:end])
    var1 = [int(chunk[5].split(" ")[2]) for chunk in chunks]
    var2 = [int(chunk[15].split(" ")[2]) for chunk in chunks]
    return var1, var2


def get_relations(var1, var2):
    nums = []
    relations = []
    for i, (v1, v2) in enumerate(zip(var1, var2)):
        if v1 < 0:
            pos, num = nums.pop()
            num += v1
            relations.append((i, pos, num))
        else:
            nums.append((i, v2))
    return relations


def get_highest(const):
    if const > 0:
        return 9, 9 - const
    else:
        return 9 + const, 9


def get_lowest(const):
    if const > 0:
        return 1 + const, 1
    else:
        return 1, 1 - const


def solve2(data):
    return find_num_with_generator(data, get_lowest)


# IO
a = input_as_lines("input.txt")


# 1st
print(solve1(a))


# 2nd
print(solve2(a))
