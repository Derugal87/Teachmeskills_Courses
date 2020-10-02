string = input('Введите строку: ')
length = len(string)
length_center = int(length / 2)
if string[length_center] == string[0]:
    print(string[1:-1])
else:
    print(string[length_center])
