def special_operations(number):
    summ = 0
    mult = 1
    for i in number:
        summ += int(i)
        mult *= int(i)
    return f'summ = {summ}, mult = {mult}'


if __name__ == '__main__':
    print(special_operations(input('Enter number: ')))
