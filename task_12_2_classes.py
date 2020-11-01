from abc import ABC, abstractmethod
from math import pi, sqrt


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y


class Figure(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass

    @abstractmethod
    def get_perimetr(self) -> float:
        pass

    @staticmethod
    def distance(point, point1) -> float:
        return sqrt(abs(point1.x - point.x) ** 2 + abs(point1.y - point.y) ** 2)

class Circle(Figure):
    def __init__(self, radius, point=Point(x=None, y=None)):
        self.point = point
        self.radius = radius

    def get_area(self):
        self.s = round((pi * self.radius ** 2), 2)
        return self.s

    def get_perimetr(self):
        return round((2 * pi * self.radius), 2)

    def __str__(self):
        return f'Circle area = {self.s}'


class Triangle(Figure):
    def __init__(self, point=Point(x=None, y=None), point2=Point(x=None, y=None), point3=Point(x=None, y=None)):
        self.point = point
        self.point2 = point2
        self.point3 = point3

    def operation(self):
        self.a = Figure.distance(self.point2, self.point)
        self.b = Figure.distance(self.point3, self.point)
        self.c = Figure.distance(self.point3, self.point2)
        return self.a, self.b, self.c

    def get_perimetr(self):
        self.operation()
        self.p = round(((self.a + self.b + self.c) / 2), 2)
        return self.p

    def get_area(self):
        self.operation()
        self.get_perimetr()
        self.s = round(sqrt((self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))), 2)
        return self.s

    def __str__(self):
        return f'Triangle area = {self.s}'


class Square(Figure):
    def __init__(self, point=Point(x=None, y=None), point2=Point(x=None, y=None)):
        self.point = point
        self.point2 = point2

    def operation(self):
        self.a = Figure.distance(self.point2, self.point)
        return self.a

    def get_perimetr(self):
        self.operation()
        self.p = round((self.a * 4), 2)
        return self.p

    def get_area(self):
        self.operation()
        self.s = round((self.a ** 2), 2)
        return self.s

    def __str__(self):
        return f'Square area = {self.s}'


