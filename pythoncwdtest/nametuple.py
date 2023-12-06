from collections import namedtuple
from math import sqrt

Point = namedtuple("Point" , ["x" , "y"])

pt1 = Point(1.0, 5.0) # pt1 = (1.0, 5.0)
pt2 = Point(2.5, 1.5) # pt2 = (2.5, 1.5)
line_length = sqrt((pt1.x - pt2.x) ** 2 + (pt1.y - pt2.y) ** 2)# line_length = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

print(line_length)

Worker = namedtuple("Work", ["job" , "salary", "workplace"])

Mike = Worker("Test" , 65000, "taiwan")

print(type(Mike))
print(Mike)
print(Mike[0])
print(Mike.job)