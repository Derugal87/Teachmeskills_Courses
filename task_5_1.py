def operation():
    x, y = input('Enter two operands: ').split(' ')
    sign = input('Input sign(+,-,*,/) or 0 for exit: \n')
    if sign == '+':
        addition(x, y)
    elif sign == '-':
        subtraction(x, y)
    elif sign == '*':
        multiplication(x, y)
    elif sign == '/':
        division(x, y)
    elif sign == '0':
        print('Bye!')
        exit(0)
    else:
        print('Incorrect sign')
        operation()


def addition(x, y):
    print(f'Result is: {int(x) + int(y)}')
    operation()


def subtraction(x, y):
    print(f'Result is: {int(x) - int(y)}')
    operation()


def multiplication(x, y):
    print(f'Result is: {int(x) * int(y)}')
    operation()


def division(x, y):
    if y == '0':
        print("You can't divide by 0")
        operation()
    else:
        print(f'Result is: {int(x) / int(y)}')
        operation()


if __name__ == '__main__':
    operation()
