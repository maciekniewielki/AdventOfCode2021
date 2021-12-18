from Common import *
import json
import math


def solve1(data):
    s = data[0]
    for snail in data[1:]:
        s = add(s, snail)
        reduce(s)
    return magnitude(s)


def reduce(s):
    step = 0
    while True:
        step += 1
        action = find_explode_or_split(s)
        if not action:
            return
        index, fun = action
        fun(s, index)


def explode(data, i):
    left_val, right_val = get_val(data, i)
    left_index, right_index = find_left(data, i), find_right(data, i)
    if left_index:
        set_val(data, left_index, get_val(data, left_index) + left_val)
    if right_index:
        set_val(data, right_index, get_val(data, right_index) + right_val)
    set_val(data, i, 0)


def split(data, i):
    half_val = get_val(data, i) / 2
    left_val, right_val = math.floor(half_val), math.ceil(half_val)
    set_val(data, i, [left_val, right_val])


def find_explode_or_split(data):
    def explode_cond(val, curr_index): return len(
        curr_index) >= 4 and isinstance(val, list)
    index = get_leftmost_index(data, explode_cond)
    if index:
        return index, explode

    def split_cond(val, curr_index): return isinstance(val, int) and val >= 10
    index = get_leftmost_index(data, split_cond)
    if index:
        return index, split

    return ()


def get_leftmost_index(data, condition):
    indexes = []
    list(traverse(data, indexes, [], condition))
    if indexes:
        return indexes[0]
    return []


def traverse(o, indexes, current_index, condition):
    if condition(o, current_index):
        indexes += [current_index]
    if isinstance(o, list):
        for i, value in enumerate(o):
            new_index = current_index[:] + [i]
            for subvalue in traverse(value, indexes, new_index, condition):
                yield subvalue
    else:
        yield o


def add(s1, s2):
    return [json.loads(str(s1)), json.loads(str(s2))]


def get_val(data, i):
    if i is None:
        return None
    for curr in i:
        try:
            data = data[curr]
        except:
            return None
    return data


def set_val(data, i, val):
    if not i:
        return
    for curr in i[:-1]:
        data = data[curr]
    data[i[-1]] = val


def find_left(data, i):
    i = i[:]
    while i:
        if i[-1] == 1:
            i = i[:-1]+[0]
            while not isinstance(get_val(data, i), int):
                i += [1]
            return i
        i.pop()

    return None


def find_right(data, i):
    i = i[:]
    while i:
        if i[-1] == 0:
            i = i[:-1]+[1]
            while not isinstance(get_val(data, i), int):
                i += [0]
            return i
        i.pop()

    return None


def magnitude(data):
    if isinstance(data, int):
        return data
    return 3 * magnitude(data[0]) + 2 * magnitude(data[1])


def solve2(data):
    m = []
    for i, snail1 in enumerate(data):
        for j, snail2 in enumerate(data):
            if i != j:
                s = add(snail1, snail2)
                reduce(s)
                mag = magnitude(s)
                m.append(mag)
    return max(m)


# IO
a = input_as_lines("input.txt")
a = [json.loads(line) for line in a]

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
