from Common import *
from collections import defaultdict


def solve(data, incl_diag):
    m = defaultdict(int)
    for point in data:
        line = get_line(point, incl_diag)
        apply_line(m, line)
    return sum([1 if m[x, y] > 1 else 0 for x, y in m])


def get_line(p, incl_diag):
    if p[0][0] == p[1][0] or p[0][1] == p[1][1]:
        return get_points(p[0], p[1])
    elif incl_diag:
        return get_points(p[0], p[1])
    else:
        return []


def apply_line(m, line):
    for x, y in line:
        m[x, y] += 1


def get_points(start, end):
    diff_x = end[0] - start[0]
    diff_y = end[1] - start[1]

    points_n = max(abs(diff_x), abs(diff_y)) + 1
    sign_x = sign(diff_x)
    sign_y = sign(diff_y)

    return [(start[0]+sign_x*i, start[1]+sign_y*i) for i in range(points_n)]


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    if x == 0:
        return 0


def to_ints(p):
    point_x, point_y = p.split(",")
    return int(point_x), int(point_y)


# IO
a = input_as_lines("input.txt")
lines = []
for line in a:
    from_p, to_p = line.split(" -> ")
    lines.append((to_ints(from_p), to_ints(to_p)))


# 1st
print(solve(lines, incl_diag=False))

# 2nd
print(solve(lines, incl_diag=True))
