from Common import *
from collections import Counter


def solve1(data):
    visited = []
    find_paths(visited, ["start"], data, "end", allow_duplicate=False)
    return len(visited)


def find_paths(visited, current_path, m, to, allow_duplicate):
    curr = current_path[-1]
    if curr == to:
        visited.append(current_path)
        return

    for cave in m[curr]:
        if cave != "start" and (not is_small(cave) or small_can_be_added(current_path, cave, allow_duplicate)):
            find_paths(visited, current_path + [cave], m, to, allow_duplicate)


def is_small(cave):
    return cave.islower()


def small_can_be_added(current_path, cave, allow_duplicate):
    if cave == "end":
        return True

    cnt = Counter(current_path)
    if cave not in cnt:
        return True
    if not allow_duplicate:
        return False

    for c in cnt:
        if cnt[c] > 1 and is_small(c):
            return False
    return True


def solve2(data):
    visited = []
    find_paths(visited, ["start"], data, "end", allow_duplicate=True)
    return len(visited)


def add_to_map(m, k, v):
    if k in m:
        m[k].append(v)
    else:
        m[k] = [v]


# IO
a = input_as_lines("input.txt")
m = {}
for line in a:
    start, end = line.split("-")
    add_to_map(m, start, end)
    add_to_map(m, end, start)


# 1st
print(solve1(m))

# 2nd
print(solve2(m))
