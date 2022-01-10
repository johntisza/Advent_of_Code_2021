from pprint import pprint
from itertools import groupby

bingo_master = []

with open('day4_bingo.txt', 'r') as f:
    
    for line in f:
        if line != '\n':
            bingo_master.append(line)
            

boards = []

picked_nums = bingo_master[0]
bingo_master.remove(picked_nums)
picked_nums = picked_nums.strip().split(',')

print('1000' in picked_nums)

for _ in range(0, (len(bingo_master)//5)):
    
    boards.append(bingo_master[:5])
    del bingo_master[:5]

final_boards = []

for board in boards:
    new_board = []
    for line in board:
        line = line.split()
        new_board.append(line)
    final_boards.append(new_board)

def check_bingo_winners(board:list):
    pass

def assign_picked_nums(final_boards:list, picked_nums:list):
    for current_num in picked_nums:
        for board in final_boards:
                for row in board:
                    for num in row:
                        pass
    # return final_boards



assign_picked_nums(final_boards, picked_nums)

