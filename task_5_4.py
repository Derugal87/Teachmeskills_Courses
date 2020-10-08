def sum_operation(number):
    summ = 1
    for i in range(2, number + 1):
        summ += 1 / i
    return '{:.2f}'.format(summ)


if __name__ == '__main__':
    print(sum_operation(int(input('Enter number: '))))
