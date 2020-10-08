def operation(some_list):
    print(f'Old list: {some_list}')
    max_number = max(some_list)
    for i in range(len(some_list)):
        if not (some_list[i] % 2):
            some_list[i] = max_number
    return f'New list: {some_list}, max_number = {max_number}.'


if __name__ == '__main__':
    print('Enter 19 elements:')
    print(operation([int(input('')) for i in range(19)]))
