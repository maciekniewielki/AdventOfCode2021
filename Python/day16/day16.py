from Common import *
import math

def solve1(data):
    return get_sum_versions(data, 0)


def get_sum_versions(data, i):
    t = check_type(data, i)
    if t == 4:
        v, t, _, i = read_literal(data, i)
        return v
    else:
        v, t, l_type, length, i = read_operator(data, i)
        sub_packets = get_all_packets_to_length(data, i, length, l_type)[0]
        values = [get_sum_versions(data, x) for x in sub_packets]
        return sum(values) + v


def get_all_packets_to_length(data, i, length, l_type):
    end = i + length
    packets_indexes = []
    if l_type == "0":
        def condition(): return i != end
    else:
        def condition(): return len(packets_indexes) < length
    while condition():
        packets_indexes.append(i)
        t = check_type(data, i)
        if t == 4:
            v, t, _, i = read_literal(data, i)
        else:
            v, t, sub_l_type, s_length, i = read_operator(data, i)
            _, i = get_all_packets_to_length(data, i, s_length, sub_l_type)
    return packets_indexes, i


def check_type(data, i):
    v, t, i = read_header(data, i)
    return t


def read_header(data, i):
    v, i = read_num(data, i, 3)
    t, i = read_num(data, i, 3)
    return v, t, i


def read_bits(data, i, n):
    return data[i:i+n], i+n


def read_num(data, i, n):
    num, i = read_bits(data, i, n)
    return int(num, 2), i


def read_literal(data, i):
    v, t, i = read_header(data, i)
    payload = ""
    group = "1"
    while group[0] == "1":
        group, i = read_bits(data, i, 5)
        payload += group[1:]

    payload = int(payload, 2)
    return v, t, payload, i


def read_operator(data, i):
    v, t, i = read_header(data, i)
    length_type, i = read_bits(data, i, 1)
    if length_type == "0":
        length, i = read_num(data, i, 15)
    if length_type == "1":
        length, i = read_num(data, i, 11)
    return v, t, length_type, length, i


def solve2(data):
    return get_value(data, 0)


def get_value(data, i):
    t = check_type(data, i)
    if t == 4:
        v, t, payload, i = read_literal(data, i)
        return payload
    else:
        v, t, l_type, length, i = read_operator(data, i)
        sub_packets, i = get_all_packets_to_length(data, i, length, l_type)
        values = [get_value(data, x) for x in sub_packets]

        if t == 0:
            return sum(values)
        if t == 1:
            return math.prod(values)
        if t == 2:
            return min(values)
        if t == 3:
            return max(values)
        if t == 5:
            return int(values[0] > values[1])
        if t == 6:
            return int(values[0] < values[1])
        if t == 7:
            return int(values[0] == values[1])


# IO
a = input_as_string("input.txt")
bits = "".join(bin(int(x, 16))[2:].zfill(4) for x in a)

# 1st
print(solve1(bits))

# 2nd
print(solve2(bits))
