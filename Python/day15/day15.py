from Common import *
import numpy as np
import networkx as nx


def solve1(data):
    vertices = set()
    g = nx.DiGraph()
    for curr_x, l in enumerate(data):
        for curr_y, _ in enumerate(l):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if valid_index(curr_x+dx, curr_y+dy, data) and abs(dx) != abs(dy) and (curr_x, curr_y, curr_x+dx, curr_y+dy) not in vertices:
                        vertices.add((curr_x, curr_y, curr_x+dx, curr_y+dy))
                        g.add_edge((curr_x, curr_y), (curr_x+dx, curr_y+dy),
                                   distance=data[curr_x+dx][curr_y+dy])

    return nx.dijkstra_path_length(g, (0, 0), (len(data)-1, len(data[0])-1), weight='distance')


def valid_index(i, j, array):
    return 0 <= i < len(array) and 0 <= j < len(array[i])


def solve2(data):
    return solve1(expand(data, 5))


def expand(data, times):
    data = np.array(data, dtype=np.int8)
    rows = []
    for i in range(1, times):
        rows.append(((data+i-1) % 9) + 1)
    data = np.vstack((data, *rows))

    cols = []
    for i in range(1, times):
        cols.append(((data+i-1) % 9) + 1)
    data = np.hstack((data, *cols))
    return data


# IO
a = input_as_lines("input.txt")
array2d = [[int(digit) for digit in line] for line in a]
# 1st
print(solve1(array2d))

# 2nd
print(solve2(array2d))
