def operation(some_list):
    count = 0
    index = 0
    for i in range(len(some_list)):
        if some_list[i] - some_list[index] == 1:
            count += 1
            index = i
        else:
            index = i
    return f'\nNumber of monotone areas = {count}'


if __name__ == '__main__':
    print(operation([int(input('Enter element: \n')) for i in range(int(input('Enter number of elements: \n')))]))
