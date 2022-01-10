horizontal = 0
depth = 0
aim = 0

with open("dive_course.txt", "r") as f:

    for line in f:

        stripped_line = line.strip()
        direction, distance = stripped_line.split()
        distance = int(distance)

        if direction == "forward":
            horizontal += distance
            depth += distance * aim
        elif direction == "up":
            aim -= distance
        elif direction == "down":
            aim += distance

print(f"Final horizontal {horizontal}\nFinal depth {depth}\nFinal aim {aim}")

print(f"Day 2 solution should be {horizontal * depth}")
