def operation(start, end):
    for number in range(start, end + 1):
        summ_1 = sum(i for i in range(1, number) if number % i == 0)
        if summ_1 in range(start, end + 1) and summ_1 > number:
            summ_2 = sum(i for i in range(1, summ_1) if summ_1 % i == 0)
            if summ_2 == number:
                return number, summ_1


if __name__ == '__main__':
    print(operation(int(input('Enter "start" number: ')), int(input('Enter "end" number: '))))
