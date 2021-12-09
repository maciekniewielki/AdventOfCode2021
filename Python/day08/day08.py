from Common import *


def solve1(data):
    s = 0
    for line in data:
        for entry in line:
            if len(entry) in unique_lengths:
                s += 1
    return s


unique_lengths = {
    2: "1",
    4: "4",
    3: "7",
    7: "8"
}


def solve2(data):
    s = 0
    for before, after in data:
        s += solve_display(before, after)
    return s


def solve_display(b, a):
    b = [normalize(word) for word in b]
    a = [normalize(word) for word in a]
    guessed = {}

    def get_remaining_of_length(length):
        return [word for word in b if len(word) == length and word not in guessed]

    # guess 1,4,7,8
    for word in b:
        if len(word) in unique_lengths:
            guessed[word] = unique_lengths[len(word)]

    letters_1 = get_letters(guessed, "1")

    # guess 6
    letters_6 = [word for word in get_remaining_of_length(6) if len(intersection(word, letters_1)) == 1][0]
    guessed[letters_6] = "6"

    # map to c
    maps_to_c = difference("abcdefg", letters_6)

    # guess 5
    letters_5 = [word for word in get_remaining_of_length(5) if maps_to_c not in word][0]
    guessed[letters_5] = "5"

    # guess 9
    letters_9 = normalize(letters_5 + maps_to_c)
    guessed[letters_9] = "9"

    # guess 0
    letters_0 = [word for word in get_remaining_of_length(6)][0]
    guessed[letters_0] = "0"

    # guess 3
    letters_3 = [word for word in get_remaining_of_length(5) if len(intersection(word, letters_1)) == 2][0]
    guessed[letters_3] = "3"

    # guess 2
    letters_2 = [word for word in get_remaining_of_length(5)][0]
    guessed[letters_2] = "2"

    out_number = int("".join([guessed[word] for word in a]))
    return out_number


def get_letters(guessed, num):
    for k in guessed:
        if guessed[k] == num:
            return k


def normalize(letters):
    return "".join(sorted(letters))


def difference(a, b):
    return normalize(set(a) - set(b))


def intersection(a, b):
    return normalize(set(a).intersection(set(b)))


# IO
a = input_as_lines("input.txt")
before = []
after = []
for line in a:
    bef, aft = line.split(" | ")
    before.append(bef.split(" "))
    after.append(aft.split(" "))

# 1st
print(solve1(after))

# 2nd
print(solve2(zip(before, after)))
