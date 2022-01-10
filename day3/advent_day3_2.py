from collections import Counter


oxygen_rating = ""
co2_rating = ""

all_lists = []

with open("day3_nums.txt", "r") as f:

    for line in f:
        stripped_line = line.strip()
        stripped_line = [x for x in str(stripped_line)]
        all_lists.append(stripped_line)


for i in range(0, 12):
    c = Counter(x[i] for x in all_lists)
    
    if c['0'] > c['1']:
        all_lists = [x for x in all_lists if x[i] == '0']
    
    else:
        all_lists = [x for x in all_lists if x[i] == '1']

    oxygen_rating = all_lists[0]

all_lists = []

with open("day3_nums.txt", "r") as f:

    for line in f:
        stripped_line = line.strip()
        stripped_line = [x for x in str(stripped_line)]
        all_lists.append(stripped_line)

for i in range(0, 12):
    c = Counter(x[i] for x in all_lists)
    
    if c['0'] > c['1']:
        all_lists = [x for x in all_lists if x[i] == '1']
    
    else:
        all_lists = [x for x in all_lists if x[i] == '0']
    
    if all_lists:
        co2_rating = all_lists[0]

oxygen_rating = ''.join(oxygen_rating)
co2_rating = ''.join(co2_rating)

oxygen_decimal = int(oxygen_rating, 2)
co2_decimal = int(co2_rating, 2)
print(f"{oxygen_decimal}...{co2_decimal}")


print(f"Life support rating...{oxygen_decimal*co2_decimal}")

