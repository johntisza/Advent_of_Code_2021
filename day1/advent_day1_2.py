num_list = []
increased_num = 0

with open("day1_nums.txt", 'r') as f:
    
    for line in f:
        stripped_line = int(line.strip())
        num_list.append(stripped_line)
        
for i in range(0, (len(num_list)-3)):
    
    if (num_list[i+1] + num_list[i+2] + num_list[i+3]) > (num_list[i] + num_list[i+1] + num_list[i+2]):
        increased_num += 1
        
print(increased_num)
