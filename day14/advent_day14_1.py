from collections import Counter
import itertools

polymer_list = []

with open("day14\day14.txt") as f:

    lines = f.read().splitlines()
    code = list(lines[0])

    polymer_list = lines[2:]


def list_to_dict(polymer_list: list):

    """assign key, value pairs derived from list in puzzle input"""

    polymer_dict = dict()

    for polymer in polymer_list:
        polymer = polymer.split(" -> ")
        polymer_dict[polymer[0]] = polymer[1]

    return polymer_dict


def extend_polymer(steps:int, code: list, polymer_dict: dict):

    """extend the original string code based by zipping uneven lists with itertools zip_longest"""

    steps = steps
    mid_let_list = []
    while steps > 0:
        for i in range(len(code) - 1):

            combined = ""
            first_let, second_let = code[i], code[i + 1]
            combined += first_let + second_let

            code_let = polymer_dict[combined]

            mid_let_list.append(code_let)

        new_list = list(itertools.zip_longest(code, mid_let_list, fillvalue=""))
        mid_let_list = []
        code = "".join([str(x) for t in new_list for x in t])

        steps -= 1

    return code


def count_letters(polymer: str):

    """count letters with collections counter and return differential between most common and least common"""

    c = Counter(polymer)

    letter_count = c.most_common()

    most_frequent = letter_count[0][1]
    least_frequent = letter_count[-1][1]

    return most_frequent - least_frequent


polymer_dict = list_to_dict(polymer_list)

# part_1_polymer = extend_polymer(10, code, polymer_dict)

# part_1 = count_letters(part_1_polymer)

# print(part_1)


part_2_polymer = extend_polymer(40, code, polymer_dict)

part_2 = count_letters(part_2_polymer)

print(part_2)