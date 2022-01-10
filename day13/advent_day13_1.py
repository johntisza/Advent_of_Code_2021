import re
import numpy as np


np.set_printoptions(threshold=np.inf, linewidth=200)

coords = []
folds = []

with open("day13.txt") as f:

    for line in f:
        line = line.strip()
        my_coords = re.findall(r"\d+\,\d+", line)
        if my_coords == []:
            folds.append(line)
        else:
            my_coords = "".join(my_coords)
            my_coords = my_coords.split(",")
            x, y = int(my_coords[0]), int(my_coords[1])

            coords.append([x, y])

folds.remove("")


def transform_folds(folds):
    """turn text into "x" or "y" and int of fold axis location"""

    fold_list = []

    for fold in folds:
        fold = fold.split()[2]
        fold = fold.split("=")
        axis, loc = fold[0], int(fold[1])
        fold_list.append([axis, loc])

    return fold_list


fold_list = transform_folds(folds)


def sheet_size(coords: list):

    """derive size of "paper" per max extents"""

    x_list = []
    y_list = []
    for pair in coords:
        x, y = pair[0], pair[1]
        x_list.append(x)
        y_list.append(y)

    x_size = max(x_list) + 1
    y_size = max(y_list) + 1

    return x_size, y_size


x_size, y_size = sheet_size(coords)


grid = np.zeros((y_size, x_size))  # the OPPOSITE of logic


def insert_puz_vals(grid: np.ndarray, coords: list):

    """add '1' values where coordinates exist"""

    char = 1
    for pair in coords:
        x, y = pair[0], pair[1]
        grid[y][x] = char
    return grid


my_grid = insert_puz_vals(grid, coords)


def fold_grid(my_grid: np.ndarray, fold_list: list):
    """fold paper along specified axis"""

    for pair in fold_list:
        
        axis, loc = pair[0], pair[1]

        if axis == "x":
            
            left = my_grid[:, :loc]
            right = my_grid[:, loc+1:]
            right = np.flip(right, axis= 1) #check axis
            my_grid = np.add(left,right)
            
            
        if axis == "y":

            top = my_grid[:loc]

            bottom = my_grid[loc + 1 :]
            bottom = np.flip(bottom,axis=0)  # check axis

            my_grid = np.add(top, bottom)


            
    return my_grid


final_grid = fold_grid(my_grid, fold_list)


def make_printable(num:int):
    
    return "#" if num >= 1 else " "

def decode(final_grid:np.ndarray):
    """get final part 2 solution print output in terminal"""

    for row in final_grid:
        print(" ".join(make_printable(val) for val in row))
        
decode(final_grid)