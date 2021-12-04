from Common import *
import numpy as np


def solve1(nums, boards):
    for num in nums:
        apply_round(num, boards)
        winners = check_winners(boards)
        if winners:
            win_board = boards[winners[0]]
            temp = np.where(win_board == -1, 0, win_board)
            return num * temp.sum()


def solve2(nums, boards):
    for num in nums:
        prev_winners = check_winners(boards)
        apply_round(num, boards)
        winners = check_winners(boards)
        if len(winners) == len(boards):
            win_last_board = boards[(set(winners) - set(prev_winners)).pop()]
            return num * np.where(win_last_board == -1, 0, win_last_board).sum()


def apply_round(num, boards):
    for i in range(len(boards)):
        boards[i] = np.where(boards[i] == num, -1, boards[i])


def check_winners(boards):
    return [i for i, board in enumerate(boards) if board_win(board)]


def board_win(board):
    for i in range(5):
        if np.all(board[i, :] == -1) or np.all(board[:, i] == -1):
            return True
    return False


# IO
a = input_as_string("input.txt")
parts = a.split("\n\n")
numbers, bingos = parts[0], parts[1:]
nums = [int(x) for x in numbers.split(",")]
boards = [[[int(x) for x in rows.split(" ") if x]
           for rows in bingo.split("\n")] for bingo in bingos]
boards = [np.array(x) for x in boards]


# 1st
print(solve1(nums, boards))

# 2nd
print(solve2(nums, boards))
