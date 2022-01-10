array = []

with open('day9.txt', 'r') as f:
    for line in f:
        current_row = []
        stripped_line = line.strip()
        for index, value in enumerate(stripped_line):
            
            current_row.append((index,int(value))) #check int
        array.append(current_row)

# print(array)
for all_lists in array:
    for tuples in all_lists:
        index, value = tuples
        