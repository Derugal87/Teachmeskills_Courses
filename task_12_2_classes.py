from abc import ABC, abstractmethod
from math import pi, sqrt


class Point:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x, self.y = x, y


class Figure(ABC):

    s = None
    p = None

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
    def __init__(self, radius, point):
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
    def __init__(self, point, point2, point3):
        self.point = point
        self.point2 = point2
        self.point3 = point3
        self.a = Figure.distance(self.point2, self.point)
        self.b = Figure.distance(self.point3, self.point)
        self.c = Figure.distance(self.point3, self.point2)

    def get_perimetr(self):
        self.p = round(((self.a + self.b + self.c) / 2), 2)
        return self.p

    def get_area(self):
        self.get_perimetr()
        self.s = round(sqrt((self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))), 2)
        return self.s

    def __str__(self):
        return f'Triangle area = {self.s}'


class Square(Figure):
    def __init__(self, point, point2):
        self.point = point
        self.point2 = point2
        self.a = Figure.distance(self.point2, self.point)

    def get_perimetr(self):
        self.p = round((self.a * 4), 2)
        return self.p

    def get_area(self):
        self.s = round((self.a ** 2), 2)
        return self.s

    def __str__(self):
        return f'Square area = {self.s}'
