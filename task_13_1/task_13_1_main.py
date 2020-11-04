from task_13_1.task_13_1_func import *
from task_13_1.task_13_1_exceptions import IndexErrorException, ValueErrorException, ChooseErrorException

while True:
    numbers = input('Enter two numbers: ').split()
    try:
        if len(numbers) != 2:
            raise IndexErrorException('You must type only 2 numbers')
        elif not (numbers[0].isdigit()) or not (numbers[1].isdigit()):
            raise ValueErrorException('x & y must be numbers')

        x = int(numbers[0])
        y = int(numbers[1])

        choose = input('Enter type operation:\n'
                       '1 - add\n'
                       '2 - sub\n'
                       '3 - mul\n'
                       '4 - div\n'
                       '0 - exit\n')

        if choose == '1':
            print(add_numbers(x, y))
        elif choose == '2':
            print(sub_numbers(x, y))
        elif choose == '3':
            print(mul_numbers(x, y))
        elif choose == '4':
            print(div_numbers(x, y))
        elif choose == '0':
            exit(0)
        else:
            raise ChooseErrorException('You have to choose such types as: 1, 2, 3, 4 or 0')

    except ChooseErrorException as ce:
        print(ce)
    except IndexErrorException as ie:
        print(ie)
    except ValueErrorException as ve:
        print(ve)
