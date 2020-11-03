from task_12_2_classes import *

point = Point(1, 1)
point2 = Point(2, 2)
point3 = Point(3, 3)

circle = Circle(5, point)
triangle = Triangle(point, point2, point3)
square = Square(point, point2)

lst = [circle, triangle, square]
for i in lst:
    i.get_area()
    print(i)
