import random
import copy


def main():
    # task 11
    print('task 11')
    n1, m1 = map(int, input('Enter size of matrix A: ').split(' '))
    n2, m2 = map(int, input('Enter size of matrix B: ').split(' '))

    print('Processing matrix A: ')
    mx_a = [[random.randrange(0, 20) for _y in range(m1)] for _x in range(n1)]
    printer(mx_a)

    print('Processing matrix B: ')
    mx_b = [[random.randrange(0, 20) for _y in range(m2)] for _x in range(n2)]
    printer(mx_b)

    menu(n1, m1, n2, m2, mx_a, mx_b)


def menu(n1, m1, n2, m2, mx_a, mx_b):
    while (choose := input('\nEnter number of task (12, 13, 14 or exit): ')) != 'exit':
        if choose == '12':
            task_12(n1, m1, n2, m2, mx_a, mx_b)
        elif choose == '13':
            task_13(n1, m1, n2, m2, mx_a, mx_b)
        elif choose == '14':
            task_14(n1, m1, mx_a)


def task_12(n1, m1, n2, m2, mx_a, mx_b):
    # task 12
    print('\ntask 12')
    mx_a = copy.deepcopy(mx_a)
    if n1 != n2 or m1 != m2:
        print("The operation 'matrices addition' can't be performed.")
    for x in range(n1):
        for y in range(m1):
            mx_a[x][y] += mx_b[x][y]
    print('Processing matrices addition:')
    printer(mx_a)


def task_13(n1, m1, n2, m2, mx_a, mx_b):
    # task 13
    print('\ntask 13')
    if m1 != n2:
        print("The operation 'matrices multiply' can't be performed.")
    else:
        result = [[0 for _x in range(m2)] for _y in range(n1)]
        for i in range(n1):
            for j in range(m2):
                for k in range(n2):
                    result[i][j] += (mx_a[i][k] * mx_b[k][j])
        print('Processing matrices multiply:')
        printer(result)


def task_14(n1, m1, mx_a):
    # task 14
    print('\ntask 14')
    mx_a = copy.deepcopy(mx_a)
    const = int(input('Enter const: '))
    for i in range(n1):
        for y in range(m1):
            mx_a[i][y] *= const
    print('Scalar multiply:')
    printer(mx_a)


def printer(matrix):
    for row in matrix:
        print(row)


if __name__ == '__main__':
    main()
