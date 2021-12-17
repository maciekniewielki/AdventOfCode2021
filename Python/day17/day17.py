from Common import *
import re


def get_max_y_for_hits_array(bounds):
    y = []
    for vx in range(bounds[1]+1):
        for vy in range(bounds[2], abs(bounds[2])+1):
            max_y, hits = check_trajectory(vx, vy, bounds)
            if hits:
                y.append(max_y)
    return y


def check_trajectory(vx, vy, bounds):
    hits = False
    x, y = 0, 0
    m = bounds[2]
    for i in range(1000):
        x += vx
        y += vy
        if vx > 0:
            vx -= 1
        elif vx < 0:
            vx += 1
        vy -= 1
        if y > m:
            m = y
        hits = hits or is_inside(x, y, bounds)
    return m, hits


def is_inside(x, y, bounds):
    return (bounds[0] <= x <= bounds[1] and bounds[2] <= y <= bounds[3])


# IO
a = input_as_string("input.txt")
bounds = [int(x) for x in re.findall(r'(-?\d+)', a)]

# 1st
y_arr = get_max_y_for_hits_array(bounds)
print(max(y_arr))

# 2nd
print(len(y_arr))
