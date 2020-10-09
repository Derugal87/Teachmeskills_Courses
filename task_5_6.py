def operation(some_list):
    count = 0
    index = 0
    for i in range(1, len(some_list)):
        if i != len(some_list) - 1:
            if not(some_list[i] - some_list[index] != 1):
                if some_list[i + 1] - some_list[i] != 1:
                    count += 1
                    index = i
            else:
                index = i
        else:
            if some_list[i] - some_list[i - 1] == 1:
                count += 1
    return f'\nNumber of monotone areas = {count}'


if __name__ == '__main__':
    # print(operation([1,2,6,1,2,7,8,9]))
    print(operation([int(input('Enter element: \n')) for i in range(int(input('Enter number of elements: \n')))]))
