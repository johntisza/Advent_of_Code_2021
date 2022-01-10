from collections import Counter

days = 80
reborn_fish = 6
new_fish = 8
day_cycle_cooldown = 2

fish_list = []

with open("day6.txt", "r") as f:
    for line in f:
        line = line.strip().split(",")
        for num in line:
            fish_list.append(int(num))
    f.close()


def fish_reproduction(fish_list: list, reborn_fish: int, new_fish: int, days: int):
    for _ in range(80):
        for index, fish_val in enumerate(fish_list):
            if fish_list[index] == 0:
                fish_list.append(new_fish)
                fish_list[index] = reborn_fish
            else:
                fish_list[index] = fish_val - 1
            
        
        # print(days, fish_list)
        print(len(fish_list))


fish_reproduction(fish_list, reborn_fish, new_fish, days)


# for _ in range(80):
    
#     new_list = []
#     for fish in fish_list:
#         if fish == 0:
#             new_list.append(6)
#             new_list.append(8)
#         else:
#             new_list.append(fish-1)
#     fish_list = new_list
#     print(len(new_list))
    