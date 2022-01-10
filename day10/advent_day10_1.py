import re
from collections import Counter

start_chars = ['(', '[', '{', '<']
end_chars = [')', ']', '}', '>']

non_discarded = set()

with open('day10.txt', 'r') as f:
    
    for line in f:
        line = line.strip()
        new_line = [str(x) for x in line]
        if new_line[-1] in start_chars:
            continue
        else:
            c = Counter(new_line)
            for (current_char, count) in c.items():
                if current_char in start_chars:
                    pass
                # if current_char in start_chars:
                #     if count %2 != 0:
                #         continue
                # elif current_char in end_chars:
                #     if count %2 != 0:
                #         continue
                #     else:
                #         non_discarded.add(line)
                        
non_discarded = list(non_discarded)

print(len(non_discarded))
print(non_discarded)
# print(non_discarded)
# total_points = 0

# for char in start_chars:
#     for lines in non_discarded:
#         for idx, value in enumerate(lines):
#             print(idx,value)