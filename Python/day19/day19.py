from Common import *
import networkx as nx


class Vect:
    @staticmethod
    def add(b1, b2):
        return (b1[0] + b2[0], b1[1] + b2[1], b1[2] + b2[2])

    @staticmethod
    def subtract(b1, b2):
        return (b1[0] - b2[0], b1[1] - b2[1], b1[2] - b2[2])

    @staticmethod
    def equals(coord1, coord2):
        return coord1[0] == coord2[0] and coord1[1] == coord2[1] and coord1[2] == coord2[2]

    @staticmethod
    def manhattan(pos1, pos2):
        return sum(abs(x1 - x2) for x1, x2 in zip(pos1, pos2))


def solve1(data):
    overlaps = {}
    for i_1, s1 in enumerate(data):
        for i_2, s2 in enumerate(data):
            if i_2 > i_1:
                res = find_relative_pos_rot(s1, s2)
                if res:
                    overlaps[(i_1, i_2)] = res

    g = nx.Graph()
    for o in overlaps:
        g.add_edge(o[0], o[1], distance=1)

    all_beacons = set()
    paths = []
    scanner_positions = []
    for i, scanner in enumerate(data):
        paths.append(nx.dijkstra_path(g, i, 0))
        for beacon_coords in scanner:
            transformed = apply_all_transformations(
                beacon_coords, paths[i], overlaps)
            all_beacons.add(transformed)
        scanner_positions.append(
            apply_all_transformations((0, 0, 0), paths[i], overlaps))
    return len(all_beacons), scanner_positions


def find_relative_pos_rot(distances_0, distances_1):
    distances_1 = get_rotated_distances(distances_1)
    for rot in distances_1:
        d1_set = set(distances_1[rot])
        for beacon_i, beacon0 in enumerate(distances_0):
            for beacon_j, beacon1 in enumerate(distances_1[rot]):
                if beacon_j <= beacon_i:
                    continue
                hits = 0
                rel_pos_guess = Vect.subtract(beacon1, beacon0)
                for b0 in distances_0:
                    if Vect.add(b0, rel_pos_guess) in d1_set:
                        hits += 1

                if hits >= 12:
                    return rel_pos_guess, rot
    return None


def apply_all_transformations(coords, path, overlaps):
    current = path[0]
    path = path[1:][::-1]
    while path:
        n = path.pop()
        if n > current:
            rel_pos, rot = overlaps[(current, n)]
            coords = apply_transformation(rot, rel_pos, coords)

        else:
            rel_pos, rot = overlaps[(n, current)]
            coords = apply_reverse_transformation(rot, rel_pos, coords)
        current = n
    return coords


def apply_transformation(rot, relative_coords, coords):
    coords = Vect.add(coords, relative_coords)
    coords = apply_reverse_rotation(rot, coords)
    return coords


def apply_reverse_transformation(rot, relative_coords, coords):
    coords = apply_rotation(rot, coords)
    coords = Vect.subtract(coords, relative_coords)
    return coords


def apply_rotation(rot, coords):
    i = rot // 4
    j = rot - 4 * i
    coords_after_6 = apply_6_way_rotations(coords)[i]
    coords_after_4 = apply_4_way_rotations(coords_after_6)[j]
    return coords_after_4


def apply_reverse_rotation(rot, coords):
    return apply_rotation(reverse_rotations[rot], coords)


def get_all_rotations(coords):
    r = []
    for rots_6 in apply_6_way_rotations(coords):
        for rots_24 in apply_4_way_rotations(rots_6):
            r += [rots_24]
    return r


def apply_6_way_rotations(coords):
    x, y, z = coords
    rots = [
        (x, y, z),
        (-x, -y, z),
        (y, -x, z),
        (-y, x, z),
        (z, y, -x),
        (-z, y, x)
    ]
    return rots


def apply_4_way_rotations(coords):
    x, y, z = coords
    rots = [
        (x, y, z),
        (x, z, -y),
        (x, -y, -z),
        (x, -z, y)
    ]
    return rots


def get_rotated_distances(scanner):
    distances = {}
    for i, b1 in enumerate(scanner):
        for rot_num, val in enumerate(get_all_rotations(b1)):
            if i == 0:
                distances[rot_num] = []
            distances[rot_num].append(val)
    return distances


def solve2(data):
    return max(Vect.manhattan(p1, p2) for p1 in data for p2 in data)


# IO
a = input_as_string("input.txt")
parts = a.split("\n\n")
scanners = []
for i, part in enumerate(parts):
    part = part.split("\n")
    scanner, positions = part[0], part[1:]
    scanners.append([])
    for pos in positions:
        x, y, z = [int(_) for _ in pos.split(",")]
        scanners[i].append((x, y, z))


# Reverse rotation lookup generation
rotations = [apply_rotation(i, [1, 2, 3]) for i in range(24)]
reverse_rotations = {}
for rot0, rotated in enumerate(rotations):
    for rot1 in range(24):
        if Vect.equals(apply_rotation(rot1, rotated), [1, 2, 3]):
            reverse_rotations[rot0] = rot1
            break

# 1st
ans1, scanner_pos = solve1(scanners)
print(ans1)


# 2nd
print(solve2(scanner_pos))
