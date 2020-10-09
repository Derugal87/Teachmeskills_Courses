def operation(some_list):
    count = 0
    index = 0
    for i in range(len(some_list)):
        if some_list[i] - some_list[index] == 1:
            if i != len(some_list) - 1:
                    if some_list[i] >= some_list[i + 1]:
                        count += 1
                        index = i
            else:
                count += 1
        else:
            index = i
    return f'\nNumber of monotone areas = {count}'


if __name__ == '__main__':
    print(operation([5,5,4,5,4,5]))
    # print(operation([int(input('Enter element: \n')) for i in range(int(input('Enter number of elements: \n')))]))
