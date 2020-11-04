from task_13_2.task_13_2_exceptions import DivideByZeroException


class Math:
    def __init__(self, x=None, y=None):
        self.x, self.y = x, y

    def add_numbers(self):
        return self.x + self.y

    def sub_numbers(self):
        return self.x - self.y

    def mul_numbers(self):
        return self.x * self.y

    def div_numbers(self):
        try:
            if self.y == 0:
                raise DivideByZeroException('You can\'t divide by zero')
            return self.x / self.y
        except DivideByZeroException as de:
            return de
