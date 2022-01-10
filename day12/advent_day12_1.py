from collections import Counter, defaultdict

neighbors = defaultdict(list)

optimized_paths = []

with open('day12.txt', 'r') as f:
    
    for line in f:
        line_list = line.strip().split('-')
        if 'start' in line_list:
            start_idx = line_list.index('start')
            del line_list[start_idx]
            line_list.insert(0, 'start')
            
            optimized_paths.insert(0, line_list)
            
        elif 'end' in line_list:
            end_idx = line_list.index('end')
            del line_list[end_idx]
            line_list.insert(1, 'end')
            
            optimized_paths.insert(-1, line_list)
        else:
            if line_list[0].islower():
                line_list[0], line_list[1] = line_list[1], line_list[0]
                optimized_paths.append(line_list)
        
        for line in f:
            a,b = line.strip().split('-')
            neighbors[a] += [b]
            neighbors[b] += [a]
            
print(neighbors)
            
def organize_paths(my_paths:list):
    optimized_paths = []
    
    start_caves = [path for path in my_paths if path[0] == 'start']
    big_caves = [path for path in my_paths if path[0].isupper()]
    small_caves = [path for path in my_paths if path[0].islower() and path[1].islower() and 'start' not in path and 'end' not in path]
    end_caves = [path for path in my_paths if path[-1] == 'end']
    
    for path in start_caves:
        optimized_paths.append(path)
    for path in big_caves:
        optimized_paths.append(path)
    for path in small_caves:
        optimized_paths.append(path)
    for path in end_caves:
        optimized_paths.append(path)
    
    for path in optimized_paths:
        print(path)
    
    return optimized_paths
    
optimized_paths = organize_paths(optimized_paths)
            

def find_paths(optimized_paths:list):
    start_caves = [path for path in optimized_paths if path[0] == 'start']
    big_caves = [path for path in optimized_paths if path[0].isupper()]
    small_caves = [path for path in optimized_paths if path[0].islower() and path[1].islower() and 'start' not in path and 'end' not in path]
    end_caves = [path for path in optimized_paths if path[-1] == 'end']
    
    path_count = 0
    clear_paths = []
    
    
    print(clear_paths)
    
    return path_count


find_paths(optimized_paths)