from Common import *


matching = {
    "{": "}",
    "[": "]",
    "(": ")",
    "<": ">"
}

error_score_map = {
    "": 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

completion_score_map = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}


def solve1(data):
    s = 0
    for line in data:
        last, _ = run_until_incorrect(line)
        s += error_score_map[last]
    return s


def run_until_incorrect(line):
    buf = []
    for c in line:
        if not buf or not is_closing(c):
            buf.append(c)
        else:
            if c == matching[buf[-1]]:
                buf.pop()
            else:
                return c, buf
    return "", buf


def is_closing(c):
    return c in [")", "]", "}", ">"]


def solve2(data):
    incomplete = [line for line in data if run_until_incorrect(line)[0] == ""]
    scores = []
    for line in incomplete:
        _, buf = run_until_incorrect(line)
        scores.append(calc_corr_score(buf))

    return sorted(scores)[len(scores) // 2]


def calc_corr_score(buf):
    score = 0
    for unmatched in buf[::-1]:
        score *= 5
        score += completion_score_map[matching[unmatched]]
    return score


# IO
a = input_as_lines("input.txt")

# 1st
print(solve1(a))

# 2nd
print(solve2(a))
