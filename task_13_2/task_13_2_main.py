from task_13_2.task_13_2_classes import *
from task_13_2.task_13_2_exceptions import IndexErrorException, ValueErrorException, ChooseErrorException


math = Math()

while True:
    numbers = input('Enter two numbers: ').split()
    try:
        if len(numbers) != 2:
            raise IndexErrorException('You must type only 2 numbers')
        elif not (numbers[0].isdigit()) or not (numbers[1].isdigit()):
            raise ValueErrorException('x & y must be numbers')
        x = int(numbers[0])
        y = int(numbers[1])

        math.x = x
        math.y = y

        choose = input('Enter type operation:\n'
                       '1 - add\n'
                       '2 - sub\n'
                       '3 - mul\n'
                       '4 - div\n'
                       '0 - exit\n')

        if choose == '1':
            print(math.add_numbers())
        elif choose == '2':
            print(math.sub_numbers())
        elif choose == '3':
            print(math.mul_numbers())
        elif choose == '4':
            print(math.div_numbers())
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
