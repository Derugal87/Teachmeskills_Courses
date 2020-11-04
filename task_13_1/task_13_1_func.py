from task_13_1.task_13_1_exceptions import DivideByZeroException


def add_numbers(a1, a2):
    return a1 + a2


def sub_numbers(a1, a2):
    return a1 - a2


def mul_numbers(a1, a2):
    return a1 * a2


def div_numbers(a1, a2):
    try:
        if a2 == 0:
            raise DivideByZeroException('You can\'t divide by zero')
        return a1 / a2
    except DivideByZeroException as de:
        return de
