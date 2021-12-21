from Common import *
from collections import Counter
import re


def solve1(starting0, starting1):
    dice = [0, 0]
    p0, p1, pos0, pos1, t = 0, 0, starting0, starting1, 0
    while True:
        p0, p1, pos0, pos1, t = turn_det(p0, p1, pos0, pos1, t, dice)
        if p0 >= 1000:
            return dice[1] * p1
        if p1 >= 1000:
            return dice[1] * p0


def turn_det(p0, p1, pos0, pos1, t, dice):
    amount = roll_det(dice) + roll_det(dice) + roll_det(dice)
    if t == 0:
        pos0 = move(pos0, amount)
        p0 += pos0
    if t == 1:
        pos1 = move(pos1, amount)
        p1 += pos1

    return p0, p1, pos0, pos1, 1 - t


def roll_det(dice):
    dice[0] += 1
    if dice[0] > 100:
        dice[0] = 1
    dice[1] += 1
    return dice[0]


def move(current, how_much):
    return (current + (how_much - 1)) % 10 + 1


def turn_quant(p0, p1, pos0, pos1, t, rolled):
    if t == 0:
        pos0 = move(pos0, rolled)
        p0 += pos0
    if t == 1:
        pos1 = move(pos1, rolled)
        p1 += pos1

    win = -1
    if p0 >= 21:
        win = 0
    if p1 >= 21:
        win = 1

    return p0, p1, pos0, pos1, 1 - t, win


def get_all_quantum_turns(p0, p1, pos0, pos1, t):
    results = []
    for die1 in range(1, 4):
        for die2 in range(1, 4):
            for die3 in range(1, 4):
                results.append(turn_quant(
                    p0, p1, pos0, pos1, t, die1 + die2 + die3))
    return results


def solve2(starting0, starting1):
    game_states = Counter()
    game_states[(0, 0, starting0, starting1, 0)] = 1
    wins = [0, 0]
    while game_states:
        for state in list(game_states.keys()):
            num_states = game_states[state]
            all_res = get_all_quantum_turns(*state)
            for result in all_res:
                *res_state, win = result
                res_state = tuple(res_state)
                if win != -1:
                    wins[win] += num_states
                else:
                    game_states[res_state] += num_states
            del game_states[state]
    return max(wins)


# IO
a = input_as_lines("input.txt")
starting0 = int(re.findall(r'(\d+)', a[0])[-1])
starting1 = int(re.findall(r'(\d+)', a[1])[-1])

# 1st
print(solve1(starting0, starting1))


# 2nd
print(solve2(starting0, starting1))
