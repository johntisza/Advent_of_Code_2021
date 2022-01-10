horizontal = 0
depth = 0

with open('dive_course.txt', 'r') as f:
    
    for line in f:
        stripped_line = line.strip()
        direction, distance = stripped_line.split()
        distance = int(distance)
        if direction == 'forward':
            horizontal += distance
        elif direction == 'up':
            depth -= distance
        elif direction == 'down':
            depth += distance
            
print(f"horizontal {horizontal}\ndepth {depth}")

print(f"{horizontal * depth}")