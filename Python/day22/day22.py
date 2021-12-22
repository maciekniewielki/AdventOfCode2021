from Common import *
import re


def solve1(data):
    limit = (-50, 50)
    on_cubes = {}
    for action in data:
        val, x, y, z = action
        overlap = get_inside_overlap((x, y, z), (limit, limit, limit))
        if not overlap:
            continue
        perform_action(val, x, y, z, on_cubes)
    return sum(on_cubes[k] for k in on_cubes)


def get_inside_overlap(b1, b2):
    x_o = get_1d_overlap(b1[0], b2[0])
    y_o = get_1d_overlap(b1[1], b2[1])
    z_o = get_1d_overlap(b1[2], b2[2])
    if x_o == None or y_o == None or z_o == None:
        return None
    return x_o, y_o, z_o


def perform_action(val, x, y, z, cubes):
    for px in range(x[0], x[1]+1):
        for py in range(y[0], y[1]+1):
            for pz in range(z[0], z[1]+1):
                cubes[(px, py, pz)] = val


def get_1d_overlap(box1, box2):
    lower = max(box1[0], box2[0])
    upper = min(box1[1], box2[1])
    if lower <= upper:
        return (lower, upper)
    return None


def solve2(data):
    cuboids = []
    for action in data:
        val, x, y, z = action
        curr_cuboid = ((x[0], x[1]+1), (y[0], y[1]+1), (z[0], z[1]+1))
        cuboids = [sub_cube for cube in cuboids for sub_cube in subdivide(
            cube, curr_cuboid)]
        if val:
            cuboids.append(curr_cuboid)

    return sum(volume(box) for box in cuboids)


def subdivide(curr_box, other_box):
    inside_overlap = get_inside_overlap(curr_box, other_box)
    if not inside_overlap:
        return [curr_box]
    if is_inside(other_box, curr_box):
        return []

    x_crosses = get_cross_points(curr_box[0], other_box[0])
    y_crosses = get_cross_points(curr_box[1], other_box[1])
    z_crosses = get_cross_points(curr_box[2], other_box[2])

    sub_boxes = []
    for x1, x2 in zip(x_crosses, x_crosses[1:]):
        for y1, y2 in zip(y_crosses, y_crosses[1:]):
            for z1, z2 in zip(z_crosses, z_crosses[1:]):
                sub_box = (x1, x2), (y1, y2), (z1, z2)
                if not is_inside(other_box, sub_box):
                    sub_boxes.append(sub_box)
    return sub_boxes


def get_cross_points(curr_line, other_line):
    points = []
    points += [curr_line[0]]
    for coord in other_line:
        if curr_line[0] < coord < curr_line[1]:
            points += [coord]
    points += [curr_line[1]]
    return points


def is_inside(b1, b2):
    return b1[0][0] <= b2[0][0] and b1[0][1] >= b2[0][1] and b1[1][0] <= b2[1][0] and b1[1][1] >= b2[1][1] and b1[2][0] <= b2[2][0] and b1[2][1] >= b2[2][1]


def length(axis):
    return axis[1] - axis[0]


def volume(box):
    return length(box[0]) * length(box[1]) * length(box[2])


# IO
a = input_as_lines("input.txt")

actions = []
for line in a:
    if line[1] == "n":
        value = 1
    else:
        value = 0
    x1, x2, y1, y2, z1, z2 = re.findall(r'(-?\d+)', line)
    actions.append((value, (int(x1), int(x2)),
                   (int(y1), int(y2)), (int(z1), int(z2))))


# 1st
print(solve1(actions))


# 2nd
print(solve2(actions))
