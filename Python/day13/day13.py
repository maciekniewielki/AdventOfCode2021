from Common import *
import re
from operator import itemgetter


def solve1(points, folds):
    paper = generate_starting_paper(points)
    paper = fold(paper, folds[0])
    return sum(sum(paper, []))


def generate_starting_paper(points):
    max_x = max(points, key=itemgetter(0))[0] + 1
    max_y = max(points, key=itemgetter(1))[1] + 1
    paper = [[True if (x, y) in points else False for y in range(max_y)]
             for x in range(max_x)]
    return paper


def print_board(paper):
    max_x = len(paper)
    max_y = len(paper[0])
    paper = [["#" if paper[x][y] else "." for y in range(
        max_y)] for x in range(max_x)]
    arr = [*zip(*paper)]
    s = ""
    for line in arr:
        s += "".join(line) + "\n"
    return s


def fold(paper, fold):
    max_y = len(paper[0])
    max_x = len(paper)
    if fold[0] == "x":
        new_paper = [[False for y in range(max_y)] for x in range(max_x//2)]
        middle_x = fold[1]
        for x in range(middle_x):
            for y in range(max_y):
                new_paper[x][y] = paper[x][y] | paper[max_x - 1 - x][y]
        return new_paper
    if fold[0] == "y":
        new_paper = [[False for y in range(max_y//2)] for x in range(max_x)]
        middle_y = fold[1]
        for x in range(max_x):
            for y in range(middle_y):
                new_paper[x][y] = paper[x][y] | paper[x][max_y - 1 - y]
        return new_paper


def solve2(points, folds):
    paper = generate_starting_paper(points)
    for f in folds:
        paper = fold(paper, f)
    return print_board(paper)


# IO
a = input_as_lines("input.txt")
points = []
folds = []
reading_points = True
for line in a:
    if not line.strip():
        reading_points = False
        continue
    if reading_points:
        start, end = re.findall(r'(\d+),(\d+)', line)[0]
        points.append((int(start), int(end)))
    else:
        along, l = re.findall(r'([xy])=(\d+)', line)[0]
        folds.append((along, int(l)))


# 1st
print(solve1(points, folds))

# 2nd
print(solve2(points, folds), end="")
