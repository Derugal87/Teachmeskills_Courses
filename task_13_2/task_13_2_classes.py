from task_13_2.task_13_2_exceptions import DivideByZeroException


class Math:
    def __init__(self, x=None, y=None):
        self.x, self.y = x, y

    def __add__(self):
        return self.x + self.y

    def __sub__(self):
        return self.x - self.y

    def __mul__(self):
        return self.x * self.y

    def __truediv__(self):
        try:
            if self.y == 0:
                raise DivideByZeroException('You can\'t divide by zero')
            return self.x / self.y
        except DivideByZeroException as de:
            return de
