from Common import *
from collections import Counter


def solve1(start, m):
    current = start
    for _ in range(10):
        current = step(current, m)
        cnt = Counter(current)

    cnt = Counter(current)
    return cnt.most_common()[0][1] - cnt.most_common()[-1][1]


def step(current, m):
    inserts = []
    for i, x in enumerate(current[:-1]):
        pair = current[i] + current[i+1]
        if pair in m:
            inserts.append((i+1, m[pair]))

    current = list(current)
    for i, letter in inserts[::-1]:
        current.insert(i, letter)

    return "".join(current)


def solve2(start, m):
    pairs_cnt = Counter()
    letter_cnt = Counter()
    for pair in m:
        pairs_cnt[pair] = 0
    for letter in start:
        letter_cnt[letter] += 1
    pairs_map = {}
    for pair in m:
        pairs_map[pair] = []
        result = pair[0] + m[pair] + pair[1]
        if result[:2] in m:
            pairs_map[pair].append(result[:2])
        if result[1:] in m:
            pairs_map[pair].append(result[1:])

    for i, x in enumerate(start[:-1]):
        pair = start[i] + start[i+1]
        if pair in m:
            pairs_cnt[pair] += 1

    for _ in range(40):
        added_this_it = Counter()
        for pair in pairs_cnt:
            pair_n = pairs_cnt[pair]
            for res in pairs_map[pair]:
                added_this_it[res] += pair_n
            added_this_it[pair] -= pair_n
            letter_cnt[m[pair]] += pair_n

        pairs_cnt += added_this_it

    return letter_cnt.most_common()[0][1] - letter_cnt.most_common()[-1][1]


# IO
a = input_as_lines("input.txt")
start, rest = a[0], a[2:]
m = {}
for line in rest:
    pair, letter = line.split(" -> ")
    m[pair] = letter

# 1st
print(solve1(start, m))

# 2nd
print(solve2(start, m))
