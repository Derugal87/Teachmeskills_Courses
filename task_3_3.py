string = input('Введите строку: ')
length = len(string)
if length > 10:
    print(f'{string}!!!')
elif length < 10:
    print(string[1])
