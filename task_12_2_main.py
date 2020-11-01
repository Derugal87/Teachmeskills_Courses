from task_12_2_classes import *

circle = Circle(5, Point(1, 1))
triangle = Triangle(Point(1,1), Point(2,2), Point(3,3))
square = Square(Point(1,1), Point(2,2))

lst = [circle, triangle, square]
for i in lst:
    i.get_area()
    print(i)

