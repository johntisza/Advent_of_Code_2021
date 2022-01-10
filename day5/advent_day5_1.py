import numpy as np
from collections import Counter

points = []

with open('day5.txt', 'r') as f:
    for line in f:
        var1, var2 = line.split(' -> ')
        x1,y1 = int(var1.split(',')[0]),int(var1.split(',')[1])
        x2,y2 = int(var2.split(',')[0]),int(var2.split(',')[1])
        
        if x1 == x2 or y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1):
                for y in range(min(y1,y2), max(y1,y2)+1):
                    points.append((x,y))
        

my_answer = 0
for (pts,count) in Counter(points).items():
        if count > 1:
            my_answer +=1
print(my_answer)
            
print(len([pts for (pts, count) in Counter(points).items() if count >1]))
