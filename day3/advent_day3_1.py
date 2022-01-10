from collections import Counter


gamma_rate = ""
epsilon_rate = ""

all_lists = []

with open("day3_nums.txt", "r") as f:

    for line in f:
        stripped_line = line.strip()
        stripped_line = [x for x in str(stripped_line)]
        all_lists.append(stripped_line)


for i in range(0, 12):
    c = Counter(x[i] for x in all_lists)
    if c["0"] > c["1"]:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"


gamma_decimal = int(gamma_rate, 2)
epsilon_decimal = int(epsilon_rate, 2)
print(f"{gamma_decimal}...{epsilon_decimal}")

print(f"{gamma_decimal*epsilon_decimal}")
