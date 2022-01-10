import math
from statistics import mean, median

crab_list = []

with open('day7.txt', 'r') as f:
    
    for line in f:
        crabs = line.strip().split(',')
        for crab in crabs:
            crab_list.append(int(crab))
    f.close()
    
print(median(crab_list))
print(mean(crab_list))

median_num = median(crab_list)

def find_pos(crab_list:list, median_num:int):
    total_fuel = 0
    
    for crab in crab_list:
        total_fuel += abs(crab-median_num)
        
    return total_fuel

print(find_pos(crab_list,median_num))